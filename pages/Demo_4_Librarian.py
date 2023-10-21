import streamlit as st
import pandas as pd
import sqlalchemy
from datetime import date
import utils
from streaming import StreamHandler
from langchain.agents import create_sql_agent, AgentExecutor, load_tools, AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from streaming import StreamHandler
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
import sqlalchemy
from bot_instructions import chatbot_instructions, sqlbot_instructions
from langchain.chains import LLMChain, SequentialChain

import warnings
warnings.filterwarnings('ignore')


# Configuration and Markdown
st.set_page_config(page_title="Librarian", page_icon="📚")
st.header("Librarian for Generative Agriculture")
st.write("Explore the raw observations by asking a question. Try, 'have we seen any bugs on our plants?'")

# Setup database and agent chain
@st.cache(allow_output_mutation=True)
def setup_chain(chatbot_instructions):
    utils.configure_openai_api_key()
    #openai_model = "gpt-3.5-turbo-instruct"
    openai_model = "gpt-3.5-turbo"
    # openai_model = "gpt-4-0613"
    #openai_model = "gpt-4-32k" # 4x context length of gpt-4
    
    # Initialize memory setup (commented out for future use)
    chatbot_memory = None  # Replace with your actual memory setup
    
    # Setup Chatbot
    chatbot_prompt_template = PromptTemplate(
        input_variables=['table_data', 'user_input'],
        template=chatbot_instructions
    )
    llm = OpenAI(model_name=openai_model, temperature=0.0, streaming=False)
    chatbot_agent = LLMChain(
        llm=llm, 
        memory=chatbot_memory, 
        prompt=chatbot_prompt_template, 
        verbose=True)
    
    return chatbot_agent

# Database Connection
username, password, host, port, database = [st.secrets[key] for key in ["username", "password", "host", "port", "database"]]
db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
# Initialize Database Connection
try:
    engine = sqlalchemy.create_engine(db_url)
    conn = engine.connect()
except Exception as e:
    st.write(f"An error occurred: {e}")
    exit()

# Agent Setup
chatbot_instructions = """You are a data assistant. Your main task is to analyze the last 10 entries from the 'raw_observations' table and provide insights based on the user's query.

User Query: {user_input}

Sample Data: 
{table_data}

Note: 
- Provide insights or summaries based on the data in 'df'.
- If the user's query suggests it, feel free to mention any patterns, anomalies, or notable points.

Please respond with **ONLY INSIGHTS** based on the last 10 entries in the 'raw_observations' table. """



chatbot_agent = setup_chain(chatbot_instructions)  # Setup bot

# Load the most recent 7 entries from raw_observations
try:
    query = "SELECT * FROM raw_observations ORDER BY time_observed DESC LIMIT 7;"
    df = pd.read_sql(query, engine)
    st.write("### Most Recent Entries in raw_observations")
    
    # Replace Base64 image strings with the word "Image"
    df['image'] = df['image'].apply(lambda x: "Image" if x else "No Image")
    st.table(df)
except Exception as e:
    st.write(f"An error occurred: {e}")

# Add chatbox for user queries
user_query = st.text_input("Ask a question about the last 10 entries:")

# Bot Interaction
if user_query:
    utils.display_msg(user_query, 'user')
    with st.chat_message("assistant"):
        st_cb = StreamHandler(st.empty())
        
        # Pass only the last 10 rows of the data to the chatbot to reduce token count
        sample_df = df.tail(10).to_dict()  # Assuming df is sorted by most recent
        
        chatbot_response = chatbot_agent.run(
            {
                'user_input': user_query,
                'table_data': sample_df  # Pass sample data
            },
            callbacks=[st_cb]
        )

        # Display the chatbot's insight
        st.code(chatbot_response, language='python')