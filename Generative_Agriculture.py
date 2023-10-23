import streamlit as st

def main():
    # Introduction
    st.write("""Revolutionizing farm and garden management by connecting **regenerative agriculture**, **generative AI**, and blockchain.
    """)

        # Vision
    st.header('Our Vision')
    st.write("""
    Three interconnected platforms ::

    - **[Gaia Go](https://generativeagriculture.streamlit.app/1_Gaia_Go_concept)**: **Pokémon Go for ecology**. Gamify ecological data collection and collect plants as unique NFTs.
    - **[Garden of Gaia](https://generativeagriculture.streamlit.app/2_Garden_of_Gaia_concept)**: **Farmville for your real-life garden**. Manage and enjoy it based on actual needs.
    - **[Farm-to-Table](https://generativeagriculture.streamlit.app/3_Blockchain_Farmers_Market_concept)**: A **blockchain-based multi-attribute marketplace** revolutionizing producer-consumer interactions to improve food security and traceability.

    Please see our [Concept Paper draft](https://generativeagriculture.streamlit.app/Concept_Paper) to see how everything fits together.

    Our immediate focus is practical tools for the Learn to Grow Educational Center, with plans for broader rollout. The Task Manager and Harvest Tracker demos are **already being used**.
    """)


    # About Us
    st.header('About Us')
    st.write("""Please see our [About page](https://generativeagriculture.streamlit.app/About) and our [GitHub](https://github.com/candrews42/generative_agriculture)
    """)

    # Live Demos
    st.header('Live Demos')
    st.write("""
    Explore these applet demos that showcase the power of AI in agriculture, all in active development:
    """)

    st.markdown("""
    For [Gaia Go](https://generativeagriculture.streamlit.app/1_Gaia_Go_concept) ::
    - [Plant Detective](https://generativeagriculture.streamlit.app/1.1_Plant_Detective_demo) :: A plant identifier that lets people identify and collect the plants around them like Pokemon Go.
    - [Librarian](https://generativeagriculture.streamlit.app/1.2_Librarian_demo) :: Trained on farm data, currently able to query recent observations from Plant Detective.

    For [Garden of Gaia](https://generativeagriculture.streamlit.app/2_Garden_of_Gaia_concept) ::
    - [Task Manager](https://generativeagriculture.streamlit.app/2.1_Task_Manager_demo) :: Shows how farm task management can be assisted by AI.
    - [Harvest Tracker](https://generativeagriculture.streamlit.app/2.2_Harvest_Tracker_demo) :: Report items harvested from the garden and add to a database
    - [Database](https://generativeagriculture.streamlit.app/2.3_Database_demo) :: Demonstrates how databases can be queried with natural language, removing the need for training in SQL or data analysis.

    For [Farm-to-Table](https://generativeagriculture.streamlit.app/3_Blockchain_Farmers_Market_concept) blockchain farmer's market ::
    - [Image Assets](https://generativeagriculture.streamlit.app/2.4_Image_Assets_demo) :: Pictures of physical farm assets can be automatically translated into digital assets for a Farmville-style interface, but for your actual farm or garden.
    Blockchain Farmer's Market
    - [Farmers Market](https://generativeagriculture.streamlit.app/3.1_Farmers_Market_demo) :: Shows how multi-attribute double-auctions can be adapted for an online farmer's market.
    
    """)

    # Meet the Founder
    st.header('Meet the Founder')
    st.write("""
    [Colin Andrews](https://generativeagriculture.streamlit.app/About) is making regenerative agriculture accessible, providing farmers and gardeners with tools, knowledge, and support to grow nutrient dense food and enhance their community's food security.  📧 [Contact](mailto:colin@generativeagriculture.com)
    """)

    # Progress
    st.header('Progress & Future')
    st.write("""
    We're a few sprints away from our first fully functional tool. We are actively **seeking funding** to **hire a developer** to productionalize our proof of concepts so that focus can be shifted to finalizing the systems design. Our system is **already being used** to gather observations, track harvests, and manage task lists on our farm, with many more functions to come, including blockchain for community-validated proof of origin and an on-chain farmer's market.""")

if __name__ == '__main__':
    main()
