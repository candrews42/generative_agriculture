# 0. Import Statements
import os
from api_keys import openai_key, postgresql_key 
from bot_instructions import chatbot_PREFIX, chatbot_FORMAT_INSTRUCTIONS, chatbot_instructions, sqlbot_instructions
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
 
from langchain.agents import create_sql_agent, AgentExecutor, load_tools, AgentType, initialize_agent
from langchain.chains import LLMChain, SequentialChain
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.utilities import WikipediaAPIWrapper

# 1. Environment Setup
# OpenAI connection
os.environ['OPENAI_API_KEY'] = openai_key
# Database Connection
db = SQLDatabase.from_uri(postgresql_key)

# 2. Setup app
st.title("Generative Agriculture Chatbot")
human_input = st.text_input("Enter your question or observation:")

# 3. Setup llms
# 3.1 Tools and Toolkit Setup
tools = load_tools(["wikipedia"], llm=OpenAI(temperature=0.1))
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0.1))

# 3.2 Memory Setup
chatbot_memory = ConversationBufferMemory(input_key='human_input', memory_key='chatbot_history')
sqlagent_memory = ConversationBufferMemory(input_key='chatbot_output', memory_key='sqlagent_history')

# 3.3 Chatbot Agent Initialization (if needed as curator)
# chatbot_agent = initialize_agent(
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     tools=tools,
#     llm=OpenAI(temperature=0.1),
#     memory=chatbot_memory,
#     agent_kwargs={
#         'prefix': chatbot_PREFIX,
#         'format_instructions': chatbot_FORMAT_INSTRUCTIONS,
#     }
# )
# chatbot_agent = initialize_agent(
#         llm=OpenAI(temperature=0.1),
#         tools=tools,
#         verbose=True,
#         memory=chatbot_memory,
#         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         agent_kwargs={
#             'prefix': chatbot_PREFIX,
#             'format_instructions': chatbot_FORMAT_INSTRUCTIONS,
#         }
#     )
chatbot_prompt_template = PromptTemplate(
    input_variables = ['human_input'],
    template=chatbot_instructions
)
sql_prompt_template = PromptTemplate(
    input_variables = ['chatbot_output'],
    template=sqlbot_instructions
)

# agent initializations
chatbot = OpenAI(temperature=0.1)
# sql_agent = OpenAI(temperature=0.1)
# TODO replace the sql agent above with the actual sql agent below:
sql_chain = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    output_key='sql_report',
    memory=sqlagent_memory,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    # agent_kwargs={
    #     'prefix': prompt_for_sql_agent
    # }
)

chatbot_chain = LLMChain(llm=chatbot, memory=chatbot_memory, output_key='chatbot_output', prompt=chatbot_prompt_template, verbose=True)
#sql_chain = LLMChain(llm=sql_agent, memory=sqlagent_memory, output_key='sql_report', prompt=sql_prompt_template, verbose=True)

# sequential_chain = SequentialChain(chains=[chatbot_chain, sql_chain], input_variables=['human_input'], output_variables=['chatbot_output', 'sql_report'], verbose=True)

# SHOW DATABASE
engine = create_engine(postgresql_key)

if human_input:
    # response = sequential_chain({'human_input':human_input})
    chatbot_output = chatbot_chain.run(human_input)
    st.write(chatbot_output)
    #st.write(response['chatbot_output'])
    sql_report = sql_chain.run(chatbot_output)    
    st.write(sql_report)
    #st.write(response['sql_report'])
    st.title('Database Table Viewer')
    if st.button('Load Table'):
        query = "SELECT * FROM task_list;"
        df = pd.read_sql(query, engine)
        st.table(df)

    with st.expander('Chatbot History'):
        st.info(chatbot_memory.buffer)
    with st.expander('SQL agent History'):
        st.info(sqlagent_memory.buffer)


