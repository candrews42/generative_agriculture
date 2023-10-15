import streamlit
import pandas as pd
import sqlalchemy

# Configuration and Markdown
streamlit.set_page_config(page_title="Database Viewer", page_icon="📊")
streamlit.markdown("# Database view")
streamlit.sidebar.header("Database")
streamlit.write("This demo shows database access to the SQL database")

# Database Connection
mode = "remote"
if mode == "remote":
    username = streamlit.secrets["username"]  # DB username
    password = streamlit.secrets["password"]  # DB password
    host = streamlit.secrets["host"]  # Public IP address for your instance
    port = streamlit.secrets["port"]
    database = streamlit.secrets["database"]  # Name of database ('postgres' by default)

db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Initialize Connection
try:
    engine = sqlalchemy.create_engine(db_url)
    conn = engine.connect()
except Exception as e:
    streamlit.write(f"An error occurred: {e}")
    exit()

# Dropdown for Table Selection
table_option = streamlit.selectbox('Choose a table', ['Select table', 'Raw Observations', 'Compost Piles', 'Compost Pile Ingredients', 'Compost Observations', 'Task List', 'Team Members', 'Plant Tracker', 'Harvest Tracker'])
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
        streamlit.table(df)
    except Exception as e:
        streamlit.write(f"An error occurred: {e}")

# SQL Query Input
sql_query = streamlit.text_area("Enter your SQL query here:", height=200)
if streamlit.button('Execute SQL Query'):
    try:
        if sql_query.lower().startswith('select'):
            df_custom = pd.read_sql(sql_query, engine)
            streamlit.table(df_custom)
        else:
            conn.execute(sql_query)
            streamlit.write("Query executed successfully.")
    except Exception as e:
        streamlit.write(f"An error occurred: {e}")