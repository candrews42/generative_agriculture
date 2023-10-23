import streamlit as st

# Set up the layout and title
st.set_page_config(page_title="Gaia Go Concept", page_icon="🌱", layout="wide")

# Header
st.title("Gaia Go - Explore, Identify, and Collect Plant NFTs")
st.subheader("Turn the world into your botanical garden.")

# Introduction
st.header("🌿 Introduction")
st.write("""
The Gaia Go app allows you to explore the world around you while identifying 
and collecting plant species as unique NFTs. Get involved in real-world challenges,
educate yourself about local flora, and contribute to a community-validated dataset.
""")

# Core Components
st.header("🛠 Core Components")

## World Map Interface
st.subheader("1. World Map Interface")
st.write("Explore the world map to find and identify plants.")
st.image("https://i.ibb.co/TLbmFBP/map.png", caption="World Map Interface")

## My Collection [PlantDex]
st.subheader("2. My Collection [PlantDex]")
st.write("Manage your unique plant NFTs and level them up by finding them in different locations.")
st.image("path/to/plantdex_placeholder.png", caption="My Collection Interface")

## Challenges Interface
st.subheader("3. Challenges Interface")
st.write("Participate in daily, weekly, and special challenges to earn rewards and contribute to the community.")
st.image("path/to/challenges_placeholder.png", caption="Challenges Interface")

# Features
st.header("⭐ Features")

## Plant Identification
st.subheader("1. Plant Identification")
st.write("Use AI to identify plants from your photos.")
st.image("path/to/plant_identification_placeholder.png", caption="Plant Identification")

## NFT Leveling Up
st.subheader("2. NFT Leveling Up")
st.write("Level up your plant NFTs by capturing them in different places.")
st.image("path/to/nft_level_placeholder.png", caption="NFT Leveling Up")

## Community-Validated Dataset
st.subheader("3. Community-Validated Dataset")
st.write("Contribute to and benefit from a community-validated dataset for plant species.")
st.image("path/to/community_validation_placeholder.png", caption="Community-Validated Dataset")

# Real Outcomes
st.header("🌍 Real Outcomes")

## Ecological Dataset
st.subheader("1. Ecological Dataset")
st.write("Contribute to a global dataset tracking plant health and distribution.")

## Community Engagement
st.subheader("2. Community Engagement")
st.write("Get communities involved in biodiversity and conservation.")

## Education
st.subheader("3. Education")
st.write("Educate users about biodiversity, ecology, and the importance of plants.")

# Tech Stack
st.header("💻 Tech Stack")
st.write("""
- Front-end: TBD
- Back-end: TBD
- Database: TBD
- Blockchain: TBD - likely Substrate or Ethereum
""")

# Conclusion
st.header("🌱 Conclusion")
st.write("""
Gaia Go offers a unique blend of technology and ecology, turning conservation into a fun and educational experience.
""")

# Contact Information
st.header("📞 Contact Information")
st.write("""
For partnerships and contributions, get in touch at [colin@generativeagriculture.com](mailto:colin@generativeagriculture.com).
""")
