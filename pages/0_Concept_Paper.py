import streamlit as st
import requests

st.title('Concept Paper')

# Objective section
# Introduction
st.write("""
# Objective

We are developing a **farm and garden management system** that integrates **regenerative agriculture, generative artificial intelligence, human observation and intervention,** and eventually NFTs and a farmer's market built on blockchain. This system is actively being tested by Learn to Grow Outdoor Educational Center—an experimental garden on the island of Bahrain. It will soon be available and useful for most farms and home gardeners.

The system aims to **collect and organize unique regional datasets and insights** while effectively managing farm operations. It focuses on sharing uncharted regenerative agriculture knowledge in the Middle East and around the world. The core codebase uses atomic AI applets to translate unstructured data into structured data, create and analyze images, and parse large datasets for insights targeted to your use. The codebase is open source under the GNU General Public License v3 and the applets are generalizable to many use cases.

# Vision

The ultimate vision of this project consists of three interconnected platforms:

- **Gaia Go**: Think Pokémon Go but for ecology. This platform aims to gamify the collection of ecological data, allowing users to explore, identify, learn, and collect plant species on a world map as unique NFTs.
- **Garden of Gaia**: Farmville for your actual garden. Manage, plan, and enjoy your garden digitally, based on real-world conditions and needs.
- **Farm-to-Table**: A blockchain-based, multi-attribute double auction marketplace for garden and farm-related items, revolutionizing the way producers and consumers interact.

In the near term, our focus is on creating practical tools for managing the regenerative farm at the Learn to Grow Educational Center that can slowly be rolled out for use in home gardens and other farms.
""")
# Background
st.write("""
# Background

Modern farming faces a critical retooling: methods like tilling and the application of pesticide have degraded soil quality, biodiversity, and nutritional density of our food. Around the world, communities must adapt to region- and community-specific challenges. In Bahrain, hot and humid summers, salty groundwater, and just 70 mm of annual rainfall necessitate reliance on external water and nutrients to restore the sandy dirt to fertile soil. Regenerative agriculture offers a hopeful path forward, principles that work in collaboration with the mechanisms of the natural world to take care of the land, increase biodiversity, and improve food quality.

Advancements in generative AI can tailor solutions to local conditions, teaming modern design thinking with methods of traditional land stewardship. Emerging AI tools such as large language models (LLMs) like ChatGPT can read and interpret natural human language to inform and organize farm management. Human observations can be collected through text or voice as unstructured data, then combined with local knowledge like plant care histories and external sources such as weather data, to create valuable structured databases, manage practical tasks, and measure and record outcomes.

# Near-Term Focus

The immediate focus is on developing a comprehensive garden task management tool. This system will allow users to add, edit, and complete tasks, and even query the system for individual task lists (e.g., specific tasks assigned to a particular gardener). This is the first phase in our multi-stage development roadmap.
""")

# Development Roadmap
st.write("""
## Development Roadmap

Each phase of development will proceed through four stages:

1. **Proof of Concept** with atomic applets
2. **Functional Use** at Learn to Grow (our pilot project)
3. **Generalization** for Multiple Users
4. **Scalability**

### Phase 2: Gaia Go Integration

**Stage 1: Proof of Concept**

- [x] User observations saved in `raw_observations` data table
- [x] Plant identification with image upload
- [ ] Location of observation pinned on map

**Stage 2: Functional Use at Learn to Grow (our pilot project)**

- [ ] Develop a mobile-friendly interface for ecological data collection
- [ ] Test the Gaia Go platform to populate our farm with plants

**Stage 3: Generalization for Multiple Users**

- [ ] Implement user accounts with customizable features
- [ ] Integrate GPS and other ease-of-use features
- [ ] Implement quests and challenges to encourage user participation

### Phase 3: Garden of Gaia Prototype

**Stage 1: Proof of Concept**

- [x] Pictures of physical farm assets can be translated into digital assets
- [ ] Garden map represented as grid for placement of plants and assets
- [ ] Plant tracker, harvest tracker database management

**Stage 2: Functional Use at Learn to Grow (our pilot project)**

- [ ] Integrate real-time tracking of garden status and tasks

**Stage 3: Generalization for Multiple Users**

- [ ] Draw on a satellite image to develop a digital twin of the real-world garden
- [ ] User engagement features like rewards for task completion
- [ ] Enable customization for different types of gardens and users

### Phase 4: Integration and Scaling

**Stage 1: Proof of Concept**

- [ ] Integrate Gaia Go, Garden of Gaia, and the Task Management Tool

**Stage 2: Functional Use at Learn to Grow (our pilot project)**

- [ ] Field test the integrated systems
- [ ] Collect data to refine and optimize the workflow

**Stage 3: Generalization for Multiple Users**

- [ ] Implement multi-location and multi-user support
- [ ] Introduce user roles and permissions for diverse needs

### Phase 5: Farm-to-Table Farmer`s Market

**Stage 1: Proof of Concept**

- [x] Mock-up of bids and offers being matched
- [ ] Multi-attribute bid and offer order book databases in .json
- [ ] Bid and offer matching mechanism

**Stage 2: Functional Use at Learn to Grow (our pilot project)**

- [ ] Learn to Grow produce searchable in database
- [ ] View and reserve produce at Learn to Grow on user interface

**Stage 3: Generalization for Multiple Users**
 
- [ ] Implement users, reviews, and community verification features

**Stage 4: Scalability**

- [ ] Blockchain integration for a transparent and decentralized marketplace
- [ ] Implement token-based rewards and incentives for marketplace participation
""")

# Project Goals and Metrics
st.write("""
## Project Goals and Metrics

### Immediate Focus

1. **AI-Integrated Regenerative Farm Management**
    - Implement AI for real-time data analysis and task management to support farm operations.
    - Metrics:
        - Reduction in number of human touches on data
        - Reduction in number of revisions of farm task list by manager

2. **Valuable Datasets and Insights from Unstructured Data**
    - Transform unstructured data such as text messages and images into structured analytics for improved farm management.
    - Metrics:
        - Accuracy rate of analytics derived from unstructured data
        - Time-efficiency gains in data collection, transformation, and interpretation

### Mid- and Long-term Objectives

1. **Enhance Educational Outcomes**
    - Use farm data and AI analytics to enhance educational programs for kids and community members.
    - Metrics:
        - Number of active experiments, points of learning in the garden
        - Educational performance indicators such as participant feedback, community involvement, and learning milestones achieved

2. **Farm-specific metrics**
    - To use easily observable or testable metrics for long-term tracking and improvement of essential farm parameters like water use, soil health, farming methods, and nutrient density of food.
    - Metrics:
        - Amount of water used, moisture content in soil, quality of water, water stored
        - Soil organic matter and stability of soil nutrients
        - Crop yield, quality, nutrient density, disease resistance, and taste
        - Documentation and recall of farm management methods
""")

# Systems Design
st.write("""
## Systems Design

### Design Principles

- **Regenerative Methods**
    - The foundation of our design principles applied to the farm and its management are grounded in the [permaculture design principles](https://permacultureprinciples.com/permaculture-principles/), the first of which being to “observe and interact”.
    - The integration is about cultivating a mindful and effective partnership with the land through appropriate interactions between humans and technology, not an over-reliance on sensors or a field of robots.

- **Data**
    - Data collection will focus on locality-specific datasets that are likely to be high value for regenerative farming in the Middle Eastern context.
    - The research will ensure that data collection ethics and practices will be studied, understood, and incorporated into the design.
    - We prioritize data sovereignty by noting all data contributors, with the intention of adding blockchain-traceable data infrastructure as the system develops.

- **Open Source**
    - The farm management system will be open source, allowing for transparency, collaboration, and adaptability, and letting the system be generalized to be applied to similar problems. All data and IP will remain protected.
""")



st.markdown("## [More to Come! Stay Tuned...]")


# System Design
st.write("""
- **System Design**
    - Modules, Components, and Interactions
    - Blockchain
""")

# Go-to-Market Plan
st.write("""
- **Go-to-Market Plan**
    - Market Research
        - Stakeholder Mapping
        - Competitive Analysis
    - Branding and Positioning
    - Marketing / Launch
    - Budget and Financials
    - Timeline / Roadmap
    - Adaptation and Feedback Loop
    - Risks
""")

# Company
st.write("""
- **Company**
    - Team
    - Company Structure and Legal
    - Investor Brief
""")

# Literature Review
st.write("""
- **Literature Review**
    - Regenerative agriculture: 
        - Issues with established farming methods
        - Environmental impact of modern technologies
        - Emergence of regenerative agriculture
    - Generative Artificial Intelligence: 
        - Technology in agriculture management
        - The established tools of generative AI
        - Bridging the physical / digital gap
""")

