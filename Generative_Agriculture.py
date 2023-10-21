import streamlit as st

def main():

    st.title('Generative Agriculture')

    # Introduction
    st.header('Farmville for your real-life garden.')
    st.write("""Revolutionizing farming and gardening by connecting **regenerative agriculture** and **generative AI**.
    """)

    # About Us
    st.header('About Us')
    st.write("""Please see our [About page](https://generativeagriculture.streamlit.app/About)
                and our [Concept Paper draft](https://generativeagriculture.streamlit.app/Concept_Paper)
    """)

    # Live Demos
    st.header('Live Demos')
    st.write("""
    Explore these exciting demos that showcase the power of AI in agriculture, all in active development:
    """)

    st.markdown("""
    - [Task Manager](https://generativeagriculture.streamlit.app/Demo_1_Task_Manager) :: Shows how farm task management can be assisted by AI.
    - [Database](https://generativeagriculture.streamlit.app/Demo_2_Database) :: Demonstrates how databases can be queried with natural language, removing the need for training in SQL or data analysis.
    - [Plant Detective](https://generativeagriculture.streamlit.app/Demo_3_Plant_Detective) :: A plant identifier that lets people identify and collect the plants around them like Pokemon Go.
    - [Librarian](https://generativeagriculture.streamlit.app/Demo_4_Librarian) :: Trained on farm data, currently able to query recent observations from Plant Detective.
    - [Farmers Market](https://generativeagriculture.streamlit.app/Demo_5_Farmers_Market) :: Shows how multi-attribute double-auctions can be adapted for an online farmer's market.
    - [Image Assets](https://generativeagriculture.streamlit.app/Demo_6_Image_Assets) :: Pictures of physical farm assets can be automatically translated into digital assets for a Farmville-style interface, but for your actual farm or garden.
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
