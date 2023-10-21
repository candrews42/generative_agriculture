import streamlit as st
import json
from streaming import StreamHandler
from langchain.agents import create_sql_agent, AgentExecutor, load_tools, AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import utils
import warnings

warnings.filterwarnings('ignore')

# Configuration and Markdown
st.set_page_config(page_title="Farmers Market Chatbot", page_icon="🌽")
st.header("Farmers Market Demo")
st.write("Welcome to the Farmers Market demo. Here, you can simulate buying or selling garden-related items.")

# Setup database and agent chain
@st.cache(allow_output_mutation=True)
def setup_chain(chatbot_instructions):
    utils.configure_openai_api_key()
    #openai_model = "gpt-3.5-turbo-instruct"
    #openai_model = "gpt-3.5-turbo"
    openai_model = "gpt-4-0613"
    #openai_model = "gpt-4-32k" # 4x context length of gpt-4
    
    # Initialize memory setup (commented out for future use)
    chatbot_memory = None  # Replace with your actual memory setup
    
    # Setup Chatbot
    chatbot_prompt_template = PromptTemplate(
        input_variables=['user_input', 'action'],
        template=chatbot_instructions
    )
    llm = OpenAI(model_name=openai_model, temperature=0.0, streaming=False)
    chatbot_agent = LLMChain(
        llm=llm, 
        memory=chatbot_memory, 
        prompt=chatbot_prompt_template, 
        verbose=True)
    
    return chatbot_agent

# Agent Setup
chatbot_instructions = """You are a digital assistant at a virtual Farmers Market. Your task is to assist the user in buying or selling items. The user is looking to {action} and has provided the following description: {user_input}. 

Turn this description into a JSON object with relevant attributes for the item. Then, provide some mock search results based on these attributes. Respond with ONLY the JSON object and mock results."""

chatbot_agent = setup_chain(chatbot_instructions)  # Setup bot

# Dropdown for Buy/Sell
action = st.sidebar.selectbox("What would you like to do?", ["Select action", "Buy", "Sell"])

# Chatbox for user query
user_query = st.text_input("Please describe what you're looking to buy or sell:")

# Bot Interaction
if user_query and action != "Select action":
    utils.display_msg(user_query, 'user')
    with st.chat_message("assistant"):
        st_cb = StreamHandler(st.empty())
        
        chatbot_response = chatbot_agent.run(
            {
                'user_input': user_query,
                'action': action
            },
            callbacks=[st_cb]
        )
        
        # Assume chatbot_response contains JSON object and mock results
        # Parse and display them here (replace the following lines with actual logic)
        st.code(chatbot_response, language='json')
        
        
        # Dropdown for user to select an option to execute the trade
        options = ["Select an option", "Carrot", "Potato"]  # Replace with actual items from mock_results
        selected_option = st.sidebar.selectbox("Select an item to execute the trade:", options)
        
        if selected_option != "Select an option":
            st.success(f"You have successfully executed a trade for {selected_option}")

