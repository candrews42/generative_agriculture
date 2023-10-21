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
st.set_page_config(page_title="Database Viewer", page_icon="📊")
st.header("Database Demo for Generative Agriculture")
st.write("This demo shows database access to the SQL database and allows natural language queries.\nSelect a database in the sidebar (try harvest tracker), and ask a question like 'how many chicken eggs did we harvest each month?'")

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
chatbot_instructions = """You are a data assistant. Your main task is to generate Python code that will help the user analyze a dataset. The dataset will be in the form of a Pandas DataFrame called 'df'. 

User Query: {user_input}

Sample Data: 
{table_data}

Note: 
- Do **NOT** create the DataFrame in your response. Assume 'df' already exists.
- Do **NOT** include any comments, imports, or explanations in your output. 
- If the query suggests it, please generate Python code for creating a relevant graph using Matplotlib and streamlit, e.g.:
    plt.plot(df['some_column'])
    st.pyplot()

Please respond with **ONLY THE PYTHON CODE** that can be directly executed to analyze 'df'. """



chatbot_agent = setup_chain(chatbot_instructions)  # Setup bot

# Dropdown for Table Selection
table_option = st.sidebar.selectbox('Choose a database', ['Select database', 'Harvest Tracker', 'Plant Tracker'])
query_map = {
    'Harvest Tracker': 'SELECT * FROM harvest_tracker;',
    'Plant Tracker': 'SELECT * FROM plant_tracker;',
}

# Execute Query and Display Table
df = None  # Initialize df to None
if table_option != 'Select database':
    query = query_map[table_option]
    try:
        df = pd.read_sql(query, engine)
        st.write(df)
    except Exception as e:
        st.write(f"An error occurred: {e}")

# Add chatbox for user queries
user_query = st.text_input("Ask a question about the data:")

# Bot Interaction
if user_query:
    utils.display_msg(user_query, 'user')
    with st.chat_message("assistant"):
        st_cb = StreamHandler(st.empty())
        
        # Pass only a sample of the data to the chatbot to reduce token count
        sample_df = df.head(5).to_dict()
        
        chatbot_response = chatbot_agent.run(
            {
                'user_input': user_query,
                'table_data': sample_df  # Pass sample data
            },
            callbacks=[st_cb]
        )

        # Assume chatbot_response is Python code to be executed
        st.code(chatbot_response, language='python')
        code_to_run = chatbot_response  # replace this with actual bot output
        
        
        # Run the generated Python code on the full DataFrame
        try:
            result = eval(code_to_run)
            # Display the result, which could be a DataFrame, Series, etc.
            st.code(result, language='python')
        except Exception as e:
            st.write(f"An error occurred while running the code: {e}")
