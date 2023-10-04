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

# Dropdown for Table Selection
table_option = st.selectbox('Choose a table', ['Select table', 'Raw Observations', 'Compost Piles', 'Compost Pile Ingredients', 'Compost Observations', 'Task List', 'Team Members', 'Plant Tracker', 'Harvest Tracker'])
query_map = {
    'Raw Observations': 'SELECT * FROM raw_observations;',
    'Compost Piles': 'SELECT * FROM compost_piles;',
    'Compost Pile Ingredients': 'SELECT * FROM compost_pile_ingredients;',
    'Compost Observations': 'SELECT * FROM compost_observations;',
    'Task List': 'SELECT * FROM task_list;',
    'Team Members': 'SELECT * FROM team_members;',
    'Plant Tracker': 'SELECT * FROM plant_tracker;',
    'Harvest Tracker': 'SELECT * FROM harvest_tracker;'
}

# Execute Query and Display Table
if table_option != 'Select table':
    query = query_map[table_option]
    try:
        df = pd.read_sql(query, engine)
        st.table(df)
    except Exception as e:
        st.write(f"An error occurred: {e}")

# SQL Query Input
sql_query = st.text_area("Enter your SQL query here:", height=200)
if st.button('Execute SQL Query'):
    try:
        if sql_query.lower().startswith('select'):
            df_custom = pd.read_sql(sql_query, engine)
            st.table(df_custom)
        else:
            result = conn.execute(sql_query)
            conn.execute("COMMIT;")  # Commit the transaction if it's a write operation
            st.write(f"Query executed successfully. Rows affected: {result.rowcount}")
    except Exception as e:
        st.write(f"An error occurred: {e}")