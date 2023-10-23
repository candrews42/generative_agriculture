import streamlit as st

# Set up the layout and title
st.set_page_config(page_title="Gaia Go Concept", page_icon="🌱", layout="wide")

# Header
st.markdown("## Gaia Go - Explore, Identify, and Collect Plant NFTs")
st.markdown("#### Turn the world into your botanical garden.")

# Introduction
st.markdown("### 🌿 Introduction")
st.write("""
Explore the world, identify and collect unique plant NFTs. Participate in real-world challenges, learn about local flora, and contribute to community-validated datasets.
""")

# Core Components
st.markdown("### 🛠 Core Components")

# World Map Interface
st.markdown("#### 1. World Map Interface")
st.write("""
Explore a dynamic world map that highlights explored and unexplored areas, both by you and the community. Embark on quests to find specific plants or discover new regions. 
""")
# Create two columns
col1, col2 = st.columns([0.5, 0.5])

# Place the world map image in the first column
with col1:
    st.image("https://i.ibb.co/TLbmFBP/map.png", caption="World Map Interface", use_column_width=True) #width=300)

# Place the zoomed-in house image in the second column
with col2:
    st.image("https://i.ibb.co/9cDK0VL/house.png", caption="Zoomed-in House Interface", use_column_width=True) #width=300)

# My Collection [PlantDex]
st.markdown("#### 2. My Collection [PlantDex]")
st.write("""
Manage your collection of unique plant NFTs. Level them up by making observations, interacting with them, or validating identifications through quests.
""")
st.image("https://i.ibb.co/PNvTrqr/nft-collection-2.png", caption="My Collection Interface", width=300)

# Challenges Interface
st.markdown("#### 3. Challenges Interface")
st.write("""
Engage in daily challenges like photographing an insect on a plant, or seasonal quests like capturing a fruiting date palm. These challenges serve as educational and engaging activities.
""")
st.image("https://i.ibb.co/6t6c39B/weekly-challenges.png", caption="Challenges Interface", width=300)

# Features
st.markdown("### ⭐ Features")

# Plant Identification
st.markdown("#### 1. Plant Identification")
st.write("""
Take pictures of plants and automatically generate a custom NFT for that plant. Initially, identify plants using an external API like PlantID. As our dataset grows, we'll train our model. Future expansions could include identifying animals and insects.
""")
st.image("https://i.ibb.co/pdKwwS9/plumeria-ai-snapshot.png", caption="Plant Identification", width=500)

# NFT Leveling Up
st.markdown("#### 2. NFT Leveling Up")
st.write("""
Level up your plant NFTs for fun, to gain tradeable value, or to earn rewards from an eventual blockchain system.
""")
st.image("https://i.ibb.co/7gyRpCv/date-palm-nft.png", caption="NFT Leveling Up", width=300)

# Community-Validated Dataset
st.markdown("#### 3. Community-Validated Dataset")
st.write("""
Combat AI-generated fake data by rewarding users to challenge submissions by exploring and documenting the real world.
""")
st.image("https://i.ibb.co/1M9qn9s/voting.png", caption="Community-Validated Dataset", width=300)

# Real Outcomes
st.markdown("### 🌍 Real Outcomes")

# Ecological Dataset
st.markdown("#### 1. Ecological Dataset")
st.write("""
Contribute to a comprehensive global dataset, tracking everything from plant health to lifecycle stages. Combined with weather data, this feeds into our Librarian chatbot.
""")

# Community Engagement
st.markdown("#### 2. Community Engagement")
st.write("""
Foster community involvement through NFT and blockchain rewards. More importantly, help people attain food security by teaching them to grow their own food.
""")

# Education
st.markdown("#### 3. Education")
st.write("""
Engage children in learning about biodiversity and ecology through daily challenges and interactive quests.
""")

# Tech Stack
st.markdown("### 💻 Tech Stack")
st.write("- Front-end: TBD\n- Back-end: TBD\n- Database: TBD\n- Blockchain: TBD")

# Conclusion
st.markdown("### 🌱 Conclusion")
st.write("Gaia Go blends technology and ecology, making conservation fun and educational.")

# Contact Information
st.markdown("### 📞 Contact Information")
st.write("[colin@generativeagriculture.com](mailto:colin@generativeagriculture.com)")
