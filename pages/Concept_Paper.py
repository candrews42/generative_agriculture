import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Fetch an image from a URL
def load_image_from_url(url):
    response = requests.get(url)
    # Debug: Check the status code and the beginning of the content
    st.write(f"Debug: Status code: {response.status_code}")
    st.write(f"Debug: First 100 bytes of the content: {response.content[:100]}")
    
    img = Image.open(BytesIO(response.content))
    return img

st.title('Concept Paper')

# Objective section
st.header('Objective')
st.markdown("""
We are developing a **farm management system** that integrates the practices of **regenerative agriculture, generative artificial intelligence, human observation and intervention,** and eventually a ******************************blockchain-based farmer’s market******************************. This system is being tested by Learn to Grow Outdoor Educational Center - an experimental garden on the island of Bahrain, and will be available and useful for most farms and home gardeners.

The system will allow gardeners and visitors to text in their observations about plant care, harvest, and other activities in the garden to a bot, which analyzes their observations to create structured database entries, e.g. “10 kg of dates harvested today”, or “the tomatoes in zone 2 are ripe for harvest”. The resulting data can be used to create a task list and extract qualitative insights about the garden, e.g. “harvest the tomatoes in zone 2” or “date harvest has increased by 5% relative to this time last year.” This system will **collect and organize unique regional datasets and insights** while effectively managing farm operations, allowing the educational team to **focus on educational outcomes and the sharing of generally uncharted regenerative agriculture knowledge in the Middle East**. The core codebase translates unstructured data into structured data used to manage tasks and will be open source and generalizable to many use cases.
""")

# Background section
st.header('Background')
st.markdown("""
Modern farming faces a critical retooling: methods like tilling and the application of pesticide have degraded soil quality, biodiversity, and nutritional density of our food. Around the world, communities must adapt to region- and community-specific challenges. In Bahrain, hot and humid summers, salty groundwater, and just 70 mm of annual rainfall necessitate reliance on external water and nutrients to restore the sandy dirt to fertile soil. Regenerative agriculture offers a hopeful path forward, principles that work in collaboration with the mechanisms of the natural world to take care of the land, increase biodiversity, and improve food quality.

Advancements in generative AI can tailor solutions to local conditions, teaming modern design thinking with methods of traditional land stewardship. Emerging AI tools such as large language models (LLMs) like ChatGPT can read and interpret natural human language to inform and organize farm management. Human observations can be collected through text or voice as unstructured data, then combined with local knowledge like plant care histories and external sources such as weather data, to create valuable structured databases, manage practical tasks, and measure and record outcomes. AI integration doesn’t mean an army of robots and sensors, but instead the appropriate level of technology for the translation of observations into practical data and actionable insights. This minimizes costs, reduces reliance on materials, machinery, manufacturing, and energy linked to fossil fuels. This feature can be applied in many scenarios where human interactions in the physical world need to be bridged into the digital space, unlocking the [potential of AI](https://www.pwc.com/m1/en/publications/potential-impact-artificial-intelligence-middle-east.html) in the Middle East and around the world.
""")

# System Design section
st.header('System Design')
st.subheader('Design Principles')
st.markdown("""
- **************Regenerative Methods:**************
    - The foundation of our design principles applied to the farm and its management are grounded in the **[permaculture design principles](https://permacultureprinciples.com/permaculture-principles/)**, the first of which being to “observe and interact”.
    - The integration is about cultivating a mindful and effective partnership with the land through **appropriate interactions between humans and technology**, not an over-reliance on sensors or a field of robots.

- ************Data:************
    - Data collection will focus on **locality-specific datasets** **that are likely to be high value for regenerative farming in the Middle Eastern context**.
    - The research will ensure that **data collection ethics** and practices will be studied, understood, and incorporated into the design.
    - We prioritize **data sovereignty** by noting all data contributors, with the intention of adding blockchain-traceable data infrastructure as the system develops.

- **Open Source:** The farm management system will be **open source**, allowing for transparency, collaboration, and adaptability, and letting the system be generalized to be applied to similar problems. All data and IP will remain protected.
""")

st.subheader("[Stay Tuned! More to Come. Until then, check out our Demos in the sidebar.]")