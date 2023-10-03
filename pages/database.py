import streamlit as st
import pandas as pd
#import altair as alt
#from urllib.error import URLError
import sqlalchemy

#from api_keys import username, password, host, port, database
mode = "remote"

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# Database view")
st.sidebar.header("Database")
st.write(
    """This demo shows database access to the sql database"""
)

# Database Connection
# db = SQLDatabase.from_uri(postgresql_key)
if mode == "remote":
    username = st.secrets["username"]  # DB username
    password = st.secrets["password"]  # DB password
    host = st.secrets["host"]  # Public IP address for your instance
    port = st.secrets["port"]
    database = st.secrets["database"]  # Name of database ('postgres' by default)

db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

try:
    engine = sqlalchemy.create_engine(db_url)
    conn = engine.connect()
    query = "SELECT * FROM task_list;"
    df = pd.read_sql(query, engine)
    st.table(df)
    st.write()
except Exception as e:
    st.write(f"An error occurred: {e}")
# finally:
#     if conn:
#         conn.close()


# @st.cache_data
# def get_UN_data():
#     AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
#     df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
#     return df.set_index("Region")


# try:
#     df = get_UN_data()
#     countries = st.multiselect(
#         "Choose countries", list(df.index), ["China", "United States of America"]
#     )
#     if not countries:
#         st.error("Please select at least one country.")
#     else:
#         data = df.loc[countries]
#         data /= 1000000.0
#         st.write("### Gross Agricultural Production ($B)", data.sort_index())

#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=["index"]).rename(
#             columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
#         )
#         chart = (
#             alt.Chart(data)
#             .mark_area(opacity=0.3)
#             .encode(
#                 x="year:T",
#                 y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#                 color="Region:N",
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )