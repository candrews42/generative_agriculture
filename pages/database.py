import streamlit as st
import pandas as pd
import sqlalchemy

# Configuration and Markdown
st.set_page_config(page_title="Database Viewer", page_icon="📊")
st.markdown("# Database view")
st.sidebar.header("Database")
st.write("This demo shows database access to the SQL database")

# Database Connection
mode = "remote"
if mode == "remote":
    username = st.secrets["username"]  # DB username
    password = st.secrets["password"]  # DB password
    host = st.secrets["host"]  # Public IP address for your instance
    port = st.secrets["port"]
    database = st.secrets["database"]  # Name of database ('postgres' by default)

db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Initialize Connection
try:
    engine = sqlalchemy.create_engine(db_url)
    conn = engine.connect()
except Exception as e:
    st.write(f"An error occurred: {e}")
    exit()

# Table Buttons
if st.button('Load Raw Observations'):
    query = "SELECT * FROM raw_observations;"
elif st.button('Load Compost Piles'):
    query = "SELECT * FROM compost_piles;"
elif st.button('Load Compost Pile Ingredients'):
    query = "SELECT * FROM compost_pile_ingredients;"
elif st.button('Load Compost Observations'):
    query = "SELECT * FROM compost_observations;"
elif st.button('Load Task List'):
    query = "SELECT * FROM task_list;"
elif st.button('Load Team Members'):
    query = "SELECT * FROM team_members;"
elif st.button('Load Plant Tracker'):
    query = "SELECT * FROM plant_tracker;"
elif st.button('Load Harvest Tracker'):
    query = "SELECT * FROM harvest_tracker;"
else:
    query = None

# Execute Query and Display Table
if query is not None:
    try:
        df = pd.read_sql(query, engine)
        st.table(df)
    except Exception as e:
        st.write(f"An error occurred: {e}")
