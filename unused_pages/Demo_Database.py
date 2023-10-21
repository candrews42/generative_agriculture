import streamlit as st
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
from your_bot_module import setup_chain, utils  # Import your bot setup and utility functions

# Configuration and Markdown
st.set_page_config(page_title="Database Viewer", page_icon="📊")
st.header("Database Demo for Generative Agriculture")
st.write("This demo shows database access to the SQL database and allows natural language queries.")

# Database Connection and Bot Setup
username = st.secrets["username"]
password = st.secrets["password"]
host = st.secrets["host"]
port = st.secrets["port"]
database = st.secrets["database"]

db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
chatbot_agent, sql_agent = setup_chain(db_url)  # Setup bot and SQL toolkit

# Dropdown for Table Selection
table_option = st.sidebar.selectbox('Choose a database', ['Select database', 'Harvest Tracker', 'Plant Tracker'])
query_map = {
    'Harvest Tracker': 'SELECT * FROM harvest_tracker;',
    'Plant Tracker': 'SELECT * FROM plant_tracker;',
}

# Execute Query and Display Table
df = None
if table_option != 'Select database':
    query = query_map[table_option]
    try:
        engine = sqlalchemy.create_engine(db_url)
        df = pd.read_sql(query, engine)
        st.write(df)
    except Exception as e:
        st.write(f"An error occurred: {e}")

# Add chatbox for user queries
user_query = st.text_input("Ask a question about the data:")

# Bot Interaction
if user_query and df is not None:
    utils.display_msg(user_query, 'user')
    with st.chat_message("assistant"):
        st_cb = StreamHandler(st.empty())
        chatbot_response = chatbot_agent.run(
            {
                'user_input': user_query,
                'table_data': df.to_dict()  # Convert DataFrame to dictionary
            },
            callbacks=[st_cb]
        )
        
        # Parse the bot's response to perform the corresponding data analysis
        # TODO: Implement this part based on the bot's response
        # For example, if bot says "Create a bar chart showing the number of dates harvested each week":
        if "bar chart" in chatbot_response and "dates harvested each week" in chatbot_response:
            df['week'] = pd.to_datetime(df['date']).dt.to_period('W')
            weekly_harvest = df.groupby('week')['dates'].sum()
            plt.bar(weekly_harvest.index.astype(str), weekly_harvest.values)
            plt.xlabel('Week')
            plt.ylabel('Dates Harvested')
            plt.title('Dates Harvested Each Week')
            st.pyplot()
