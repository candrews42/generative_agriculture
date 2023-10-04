# 0. Import Statements
import os
import utils
# from api_keys import openai_key, postgresql_key 
from bot_instructions import chatbot_PREFIX, chatbot_FORMAT_INSTRUCTIONS, chatbot_instructions, sqlbot_instructions
import streamlit as st
import pandas as pd
# from sqlalchemy import create_engine
from streaming import StreamHandler
 
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
from sqlalchemy import create_engine
# import psycopg2

import streamlit as st
import os



# 2. Setup Streamlit app
st.set_page_config(page_title="GenAg Chatbot", page_icon="🌱", layout="wide")
st.header("Generative Agriculture Chatbot")
st.write("Natural language farm management tool")
# human_input = st.text_input("Enter your question or observation:")


class generative_agriculture:
    def __init__(self):
        # os.environ['OPENAI_API_KEY'] = openai_key
        utils.configure_openai_api_key()
        #self.openai_model = "gpt-3.5-turbo-instruct"
        #self.openai_model = "gpt-3.5-turbo"
        self.openai_model = "gpt-4-0613"
        # self.openai_model = "gpt-4-32k" # 4x context length of gpt-4
       
    @st.cache_resource
    def setup_chain(_self):
        # Database Connection
        # db = SQLDatabase.from_uri(postgresql_key)
        # username = st.secrets["username"]  # DB username
        # password = st.secrets["password"]  # DB password
        # host = st.secrets["host"]  # Public IP address for your instance
        # port = st.secrets["port"]
        # database = st.secrets["database"]  # Name of database ('postgres' by default)
        mode = "remote"
        # from api_keys import username, password, host, port, database

        if mode == "remote":
            username = st.secrets["username"]  # DB username
            password = st.secrets["password"]  # DB password
            host = st.secrets["host"]  # Public IP address for your instance
            port = st.secrets["port"]
            database = st.secrets["database"]  # Name of database ('postgres' by default)

        db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
        print("setting up SQL database connection")
        print(db_url)
        db = SQLDatabase.from_uri(db_url)
        print("database connection complete")
        # 3. Setup llms
        # 3.1 Tools and Toolkit Setup
        # tools = load_tools(["llm-math"], llm=OpenAI(temperature=0.1))
        toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

        # 3.2 Memory Setup
        chatbot_memory = ConversationBufferMemory()# input_key='human_input', memory_key='chatbot_history')
        sqlagent_memory = ConversationBufferMemory() #input_key='chatbot_output', memory_key='sqlagent_history')

        
        llm=OpenAI(model_name=_self.openai_model, temperature=0.1, streaming=True)
        # initialize bot instruction templates
        # chatbot_prompt_template = PromptTemplate(
        #     input_variables = ['human_input'],
        #     template=chatbot_instructions
        # )
        # sql_prompt_template = PromptTemplate(
        #     input_variables = ['chatbot_output'],
        #     template=sqlbot_instructions
        # )
        # initialize agents
        # chatbot_agent = LLMChain(
        #     llm=llm, 
        #     memory=chatbot_memory, 
        #     prompt=chatbot_prompt_template, 
        #     verbose=True)
        # sql agent initialization
        sql_agent = create_sql_agent(
            llm=OpenAI(temperature=0),
            toolkit=toolkit,
            verbose=True,
            # memory=sqlagent_memory,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            # agent_kwargs={
            #     'prefix': prompt_for_sql_agent
            # }
        )
        # memory = ConversationBufferMemory()
        # llm = OpenAI(model_name=_self.openai_model, temperature=0, streaming=True)
        # chatbot_agent = ConversationChain(llm=llm, memory=memory, verbose=True)
        
        return sql_agent #, sql_agent
    
    @utils.enable_chat_history
    def main(self):
        sql_agent = self.setup_chain()
        # chatbot_agent, sql_agent = self.setup_chain()
        user_query = st.chat_input(placeholder="Enter your observation or question about the farm")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                sql_agent_response = sqlbot_instructions.format(query_request=user_query)
                sql_response = sql_agent.run(sql_agent_response, callbacks=[st_cb])
                # sql_response = sql_agent.run(chatbot_response, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": sql_response})
                st.rerun()
                # else:
                #    chatbot_response = chatbot_agent.run(user_query, callbacks=[st_cb])
                #    st.session_state.messages.append({"role": "chatbot", "content": chatbot_response})
        # TODO add table view
        #         st.title('Database Table Viewer')
        #         if st.button('Load Table'):
        #             query = "SELECT * FROM task_list;"
        #             df = pd.read_sql(query, engine)
        #             st.table(df)



if __name__ == "__main__":
    obj = generative_agriculture()
    obj.main()

# # chatbot agent initializations
# chatbot = OpenAI(temperature=0.1)
# chatbot_agent = LLMChain(
#     llm=chatbot, 
#     memory=chatbot_memory, 
#     output_key='chatbot_output', 
#     prompt=chatbot_prompt_template, 
#     verbose=True)
# chatbot_agent = initialize_agent(
#         llm=OpenAI(temperature=0.1),
#         tools=tools,
#         toolkit=toolkit,
#         verbose=True,
#         memory=chatbot_memory,
#         output_key='chatbot_output', 
#         prompt=chatbot_prompt_template, 
#         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         agent_kwargs={
#             'prefix': chatbot_PREFIX,
#             'format_instructions': chatbot_FORMAT_INSTRUCTIONS,
#         }
#     )


# # sql agent initialization
# sql_agent = create_sql_agent(
#     llm=OpenAI(temperature=0),
#     toolkit=toolkit,
#     verbose=True,
#     output_key='sql_report',
#     memory=sqlagent_memory,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     # agent_kwargs={
#     #     'prefix': prompt_for_sql_agent
#     # }
# )


# if human_input:
#     # response = sequential_chain({'human_input':human_input})
#     chatbot_output = chatbot_agent.run(human_input)
#     st.write(chatbot_output)
#     if st.button('continue'):
#         #st.write(response['chatbot_output'])
#         sql_report = sql_agent.run(chatbot_output)    
#         st.write(sql_report)
#         #st.write(response['sql_report'])


#         

#            with st.expander('Chatbot History'):
#                st.info(sql_agent.memory)
#         with st.expander('SQL agent History'):
#             st.info(sqlagent_memory.buffer)
