import streamlit as st

# Set up the layout and title
st.set_page_config(page_title="About", page_icon="🌱", layout="wide")

# Create columns for layout
col1, col2 = st.columns([1, 3])

# Column 1: Display the profile image
profile_image_url = "https://media.licdn.com/dms/image/D4D03AQEGjcJmBU8JGw/profile-displayphoto-shrink_800_800/0/1695462094237?e=1703116800&v=beta&t=hOlAfX3j-JZZzl4sIfEgsq6R_vaaPME5TjfiS3wPYmw"
col1.image(profile_image_url, caption="Colin Andrews", width=300)

# Introduction
st.write("""
**Colin Andrews**  is the farm manager at Learn to Grow Outdoor Educational Center and Regenerative Farm, applying modern systems engineering to natural processes to build methods that directly address several UN sustainable development goals and are immediately useful to regenerating the ecology of Bahrain and the Gulf region.

Colin has had a diverse career in **strategy consulting and analytics for global end-to-end supply chain, systems engineering for blockchain-based local energy communities**, and the **integration of artificial intelligence algorithms into energy market trading**. He is just as comfortable coding on an overnight train in India, getting his hands dirty on a farm in Bahrain, and presenting in a New York City board room.
""")

# Professional Background
st.header("Education")
st.write("""
**Georgia Institute of Technology**
- **Master's in Computer Science**: machine learning and artificial intelligence.
- **Bachelor's in Electrical Engineering**: signals and systems
- **Minor Engineering & Business Management** through Denning Technology & Management Program \n
**Oregon State University**: Permaculture Design Consultant Professional Certification
""")

# Experience
st.header("Work Experience")
st.write("""
**[Learn to Grow](https://instagram.com/learntogrow.bh?igshid=MzRlODBiNWFlZA==)** :: Regenerative Farm Manager and Permaculture Design Consultant :: **Bahrain 2023**

**[Grid Singularity](https://gridsingularity.com)** :: Research Scientist in energy market design and decentralization. Designed and implemented a multi-attribute double-sided auction for local energy communities. :: **Berlin & Lisbon 2019-2022**

**[Freeel.io](https://freeel.io/)** :: Incentive Design and token engineering for Clean Energy Ecosystems. ::**Vienna 2019**

**[Kurt Salmon, part of Accenture Strategy](https://www.accenture.com/us-en/about/strategy-index)** :: Business and Analytics Strategy Consultant for end-to-end supply chain analytics and optimization. :: **New York & Atlanta, USA 2015-2018**
""")

# Articles & Contributions
st.header("Articles & Contributions")
st.write("""
- [Discussion Paper: Grid Singularity's Implementation of Symbiotic Energy Markets](https://gridsingularity.medium.com/discussion-paper-grid-singularitys-implementation-of-symbiotic-energy-markets-bd3954af43c8)
- [Fractal Ownership: A Token Engineering Concept](https://medium.com/p/54e7edc58953)
""")

# Skills & Technologies
st.header("Skills")
st.write("""
- **Programming**: Python, API Integration (ChatGPT, Langchain, MongoDB, etc.), Streamlit, AI and ML Libraries (Tensorflow, Sci-kit learn), basic AWS and Google Cloud integration, SQL and PostgreSQL
- **Product-Building Skills**: Systems Design, Prototyping, Requirements Engineering, Systems Design, Presentation
- **Business Skills**: Team Leadership and Management, Data Analysis, Presentation
- **Agri Skills**: Basic carpentry, basic electronics, composting and soil building, farm and taks management, and permaculture techniques
- **Languages**: English (native), German (proficient), Portuguese & Spanish (functional), Arabic (beginner)
""")

# Contact & Social Media
st.header("Contact")
st.write("""
- 📧 Email: [colin@generativeagriculture.com](mailto:colin@generativeagriculture.com)
- 🌐 [LinkedIn](https://www.linkedin.com/in/andrewsco/)
- 🐱 [GitHub](https://github.com/candrews42/generative_agriculture) 
- 📸 [Instagram: Learn to Grow](https://instagram.com/learntogrow.bh?igshid=MzRlODBiNWFlZA==)
""")

