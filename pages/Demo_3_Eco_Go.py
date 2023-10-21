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
st.set_page_config(page_title="Plant Collection", page_icon="🌱")
st.header("Plant Collection App")
st.write("Explore and collect unique plants around you.")

# User Inputs     
user_name = st.text_input("Your name:")    
location = st.text_input("Location:", "Current Location")   
time_observed = st.date_input("Time (default to now):", min_value=datetime.today())
notes = st.text_input("Any observations?")
uploaded_image = st.file_uploader("Upload an image of the plant:", type=['jpg', 'jpeg', 'png'])
st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)


# Store Raw Observation in Database
if st.button("Submit Observation"):
    try:
        # Convert uploaded image to bytes and then to base64 string
        base64_image = ""
        if uploaded_image:
            image_bytes = uploaded_image.read()
            base64_image = base64.b64encode(image_bytes).decode()

        # Define your query with named placeholders in a single line
        query = "INSERT INTO raw_observations (image, notes, location, time_observed, user_name) VALUES (:image, :notes, :location, :time_observed, :user_name)"

        # Create a dictionary of parameters
        params = {
            'image': base64_image if uploaded_image else None,  # Handle the case when no image is uploaded
            'notes': notes,
            'location': location,
            'time_observed': time_observed,
            'user_name': user_name
        }

        # Execute the query
        with engine.connect() as conn:
            conn.execute(sqlalchemy.text(query), params)

        st.success("Raw observation stored successfully!")
        
        if uploaded_image:
            # Initialize success flag and API response
            success = False
            api_response = {}
            
            # PlantNet API logic
            plantnet_api_key = st.secrets["plantnet_api_key"]
            PROJECT = "all"
            api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={plantnet_api_key}"

            try:
                st.write("Making API call to PlantNet...")  # Debug line
                
                # Prepare data and files for PlantNet API request
                # data = {'organs': ['auto']}
                files = [('images', ('uploaded_image', image_bytes))]

                # Make API request
                response = requests.post(api_endpoint, files=files) #, data=data)
                api_response = json.loads(response.text)
                
                # st.write(f"API Response: {api_response}")  # Debug line

                # Display the best match and potential matches
                best_match = api_response.get('bestMatch', 'Unknown')
                results = api_response.get('results', [])
                st.write(f"**Best Match: {best_match}**")
                st.write("### Potential Matches:")
                results = sorted(results, key=lambda x: x['score'], reverse=True)[:5]
                for result in results:
                    scientific_name = result['species'].get('scientificName', 'Unknown')
                    common_names = ', '.join(result['species'].get('commonNames', ['Unknown']))
                    score = result.get('score', 0)
                    st.write(f"**Scientific Name**: {scientific_name}")
                    st.write(f"**Common Names**: {common_names}")
                    st.write(f"**Score**: {score}")
                    st.write("---")

                # Assuming the API response contains 'plant_name' and 'details'
                if 'plant_name' in api_response and 'details' in api_response:
                    success = True
                
            except Exception as e:
                st.write(f"An error occurred during PlantNet API call: {e}")
            if success:
                # Insert into user_collection
                query = """INSERT INTO user_collection (user_name, plant_name, details)
                           VALUES (:user_name, :plant_name, :details)"""

                params = {
                    'user_name': user_name,
                    'plant_name': api_response['plant_name'],
                    'details': api_response['details']
                }

                with engine.connect() as conn:
                    conn.execute(sqlalchemy.text(query), params)

                st.success(f"Identified plant: {api_response['plant_name']}. Added to your collection!")
                
    except Exception as e:
        st.write(f"An error occurred: {e}")