# Import required libraries
import os
import utils
import streamlit as st
from langchain.agents import create_sql_agent, AgentExecutor, load_tools, AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from streaming import StreamHandler
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_experimental.sql import SQLDatabaseChain
# from langchain_experimental.sql import SQLDatabaseChain

# Streamlit page setup
st.set_page_config(page_title="GenAg Chatbot", page_icon="🌱", layout="wide")
st.title("Generative Agriculture Chatbot 🌱")
st.write("Natural language farm management tool")
st.sidebar.header("Quick Actions")

# Quick action buttons in sidebar
if st.sidebar.button('Count Chicken Eggs'):
    st.write("Query to count chicken eggs in the harvest table here.")
if st.sidebar.button('List Active Tasks'):
    st.write("Query to list active tasks here.")
if st.sidebar.button('Add a Task'):
    task = st.sidebar.text_input("Task Description:")
    if task:
        st.write(f"Added task: {task}")

# Define the main class for the Generative Agriculture Chatbot
class GenerativeAgriculture:
    # Initialize chatbot settings and API keys
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-instruct"
        #self.openai_model = "gpt-3.5-turbo"
        #self.openai_model = "gpt-4-0613"
        # self.openai_model = "gpt-4-32k" # 4x context length of gpt-4

    # Setup database and agent chain
    @st.cache_resource
    def setup_chain(_self):
        # Database Connection
        username, password, host, port, database = [st.secrets[key] for key in ["username", "password", "host", "port", "database"]]
        db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
        db = SQLDatabase.from_uri(db_url)
        
        # Initialize memory setup (commented out for future use)
        # chatbot_memory = ConversationBufferMemory()
        # sqlagent_memory = ConversationBufferMemory()
        
        # Setup SQL toolkit and agent
        toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
        sql_agent = create_sql_agent(
            llm=OpenAI(temperature=0.1, streaming=True),
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )
        return sql_agent
    
    # Main function to handle user input and chatbot response
    @utils.enable_chat_history
    def main(self):
        sql_agent = self.setup_chain()
        user_query = st.text_input("Enter your observation or question about the farm:", key="user_input")
        if st.button('Send'):
            with st.expander("Chat History", expanded=True):
                st.write(f"You: {user_query}")
                st.write("Chatbot is processing...")
            # TODO: Add user_query to raw_observations table
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                sql_agent_response = f"INSERT INTO raw_observations (observation) VALUES ('{user_query}');"
                sql_response = sql_agent.run(sql_agent_response, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": sql_response})
                st.rerun()

# Entry point of the application
if __name__ == "__main__":
    obj = GenerativeAgriculture()
    obj.main()
