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
st.set_page_config(page_title="Plant Detective", page_icon="🌱")
st.subheader("Plant Detective 🌱")
st.write("""
**Discover and collect unique flora in your surroundings.**

**How to Use:**
- Enter your observation in the text box below.
- Optionally, upload an image for automatic plant identification.

**What Happens Next:**
- Your observation contributes to our raw observations database.
- This database helps train our AI-powered plant librarian.
""")


# User Inputs     
user_name = st.text_input("Your name:")    
location = st.text_input("Location:", "Learn to Grow Educational Center, Bahrain")   
time_observed = st.date_input("Time (default to now):", min_value=datetime.today())
notes = st.text_input("Any observations?")
uploaded_image = st.file_uploader("Upload an image of the plant:", type=['jpg', 'jpeg', 'png'])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)


# Store Raw Observation in Database
if st.button("Submit Observation"):
    try:
        last_inserted_id = None
        # Debug: Check Database Connection
        with engine.connect() as conn:
            st.write("Database connected successfully!")
        
        # Convert uploaded image to bytes and then to base64 string
        base64_image = ""
        if uploaded_image:
            image_bytes = uploaded_image.read()
            base64_image = base64.b64encode(image_bytes).decode()

        # Define your query with named placeholders in a single line
        query = "INSERT INTO raw_observations (image, notes, location, time_observed, user_name) VALUES (:image, :notes, :location, :time_observed, :user_name) RETURNING id"
        # Create a dictionary of parameters
        params = {
            'image': base64_image if uploaded_image else None,
            'notes': notes,
            'location': location,
            'time_observed': time_observed,
            'user_name': user_name
        }

        query += " RETURNING id"
        # Debug: Print Query and Params
        # st.write(f"Executing query: {query}")

        # Execute the query
        with engine.connect() as conn:
            try:
                # Using named placeholders in SQL query
                query = "INSERT INTO raw_observations (image, notes, location, time_observed, user_name) VALUES (:image, :notes, :location, :time_observed, :user_name) RETURNING id"  # <-- MODIFIED CODE

                # Debugging: Print the query and params before executing
                # st.write(f"Debug: SQL Query to execute: {query}")
                debug_params = {k: v if k != 'image' else 'IMAGE_CONTENT_HIDDEN' for k, v in params.items()}
                st.write(f"Executing Query with Parameters: {debug_params}")

                # Execute the query with named parameters
                result = conn.execute(sqlalchemy.text(query), params)
                last_inserted_id = result.fetchone()[0]
                
                # Debugging: Print the result of the SQL execution
                # st.write(f"Debug: SQL Query executed, result: {result}")

                # Commit the transaction
                conn.commit()
                
                st.success("Raw observation stored successfully!")
            except Exception as execute_error:
                st.write(f"Debug: An error occurred during query execution: {execute_error}")
                conn.rollback()  # Rollback in case of errors

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
                
                if success:
                    try:
                        # Debugging: Print the query and parameters before executing the INSERT
                        st.write("Debug: Inserting into user_collection")
                        
                        query = """INSERT INTO user_collection (user_name, plant_name, details)
                                VALUES (:user_name, :plant_name, :details)"""

                        params = {
                            'user_name': user_name,
                            'plant_name': api_response['plant_name'],
                            'details': api_response['details']
                        }

                        debug_params = {k: v for k, v in params.items()}
                        st.write(f"Debug: SQL Insert Query: {query}")
                        st.write(f"Debug: Insert Parameters: {debug_params}")

                        # Execute the INSERT query
                        with engine.connect() as conn:
                            conn.execute(sqlalchemy.text(query), params)
                        st.success(f"Identified plant: {api_response['plant_name']}. Added to your collection!")

                        # Debugging: Preparing to execute the UPDATE query
                        st.write("Debug: Preparing to execute the UPDATE query")
                        
                        update_query = """UPDATE raw_observations SET plant_guess_scientific_name = :scientific_name,
                                        plant_guess_common_name = :common_name,
                                        plant_guess_certainty = :certainty
                                        WHERE id = :last_id"""

                        best_match = api_response.get('bestMatch', {})
                        
                        update_params = {
                            'scientific_name': best_match['species'].get('scientificName', 'Unknown'),
                            'common_name': ', '.join(best_match['species'].get('commonNames', ['Unknown'])),
                            'certainty': best_match.get('score', 0),
                            'last_id': last_inserted_id
                        }
                        
                        debug_update_params = {k: v for k, v in update_params.items()}
                        st.write(f"Debug: SQL Update Query: {update_query}")
                        st.write(f"Debug: Update Parameters: {debug_update_params}")

                        # Execute the UPDATE query
                        with engine.connect() as conn:
                            conn.execute(sqlalchemy.text(update_query), update_params)
                            conn.commit()
                            
                        st.success(f"Updated raw observations with the best match!")

                    except Exception as execute_error:
                        st.write(f"Debug: An error occurred during query execution: {execute_error}")
                        conn.rollback()  # Rollback in case of errors

                
            except Exception as e:
                st.write(f"An error occurred during PlantNet API call: {e}")
            
    except Exception as e:
        st.write(f"An error occurred: {e}")