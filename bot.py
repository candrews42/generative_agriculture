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
# from langchain_experimental.sql import SQLDatabaseChain
# from langchain_experimental.sql import SQLDatabaseChain

# Streamlit page setup
st.set_page_config(page_title="GenAg Chatbot", page_icon="🌱") #, layout="wide")
st.header("Generative Agriculture Chatbot")
st.write("Natural language farm management tool")

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
        user_query = st.chat_input(placeholder="Enter your observation or question about the farm")
        if user_query:
            utils.display_msg(user_query, 'user')
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
