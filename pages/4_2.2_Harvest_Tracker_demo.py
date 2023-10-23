import streamlit as st
import sqlalchemy
from datetime import datetime
import requests
import json
import base64

# Database Connection
username, password, host, port, database = [st.secrets[key] for key in ["username", "password", "host", "port", "database"]]
db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = sqlalchemy.create_engine(db_url)

# Configuration and Markdown
st.set_page_config(page_title="Harvest Tracker", page_icon="🌾")
st.subheader("Harvest Tracker 🌾")
st.write("""
**Track your farm's harvest efficiently.**

**How to Use:**
- Fill in the details of your harvest in the form below.
- Optionally, upload an image for record-keeping.
- Your entry will be added to the database.
""")

# User Inputs     
item = st.text_input("Item harvested (e.g., chicken eggs, mulberries):")    
harvest_date = st.date_input("Harvest date:")
quantity = st.number_input("Quantity:", min_value=0, format="%d")
unit = st.selectbox("Unit:", ["unit", "kg", "gms", "box"])
notes = st.text_input("Any additional notes?")
uploaded_image = st.file_uploader("Upload an image (optional):", type=['jpg', 'jpeg', 'png'])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

# Store Harvest Details in Database
if st.button("Submit Harvest"):
    try:
        with engine.connect() as conn:
            st.write("Database connected successfully!")

            # Convert uploaded image to bytes and then to base64 string
            base64_image = ""
            if uploaded_image:
                image_bytes = uploaded_image.read()
                base64_image = base64.b64encode(image_bytes).decode()

            query = """INSERT INTO harvest_tracker (item, harvest_date, quantity, unit, notes, image)
                    VALUES (:item, :harvest_date, :quantity, :unit, :notes, :image)"""

            params = {
                'item': item,
                'harvest_date': harvest_date,
                'quantity': quantity,
                'unit': unit,
                'notes': notes,
                'image': base64_image if uploaded_image else None,
            }

            # Execute the query
            conn.execute(sqlalchemy.text(query), params)
            conn.commit()

            st.success("Harvest details stored successfully!")
    except Exception as e:
        st.write(f"An error occurred: {e}")
