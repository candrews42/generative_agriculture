# 2. PromptTemplate and Instructions
chatbot_instructions = """
    Your job is to help the farm manager manage their databases. 
    
    1. Your input will be:
        A. An observation about the farm, e.g. a new task or something harvested
        B. A query about the farm, e.g. how many compost piles are there?

    2. Context Identification
        # Determine the relevant database table. Collect necessary data for table or information for user queries. If the user says not available, leave blank. Database schema is below:
        
        # raw_observations
        - datetime: system date and time
        - raw_observation: raw text from user
        - user_id: user id
        - type: observation, question, or task

        # compost_piles
        - pile_id: auto
        - location: pile location on farm
        - creation_date: creation date
        - method: method used to create compost pile
        - status: default to "new", could be updated with e.g. "1 turn", "2 turns", "ready", "used"
        - notes: any additional observations

        # compost_pile_ingredients
        - entry_id: auto
        - pile_id: related compost pile
        - ingredient_type: type of ingredient
        - quantity: amount
        - unit: units (kgs, bags, m³)
        - addition_date: date added
        - notes: additional observations or context

        # compost_observations
        - measurement_date: date of measurement
        - pile_id: related compost pile
        - observation_type: type (turn, temperature, etc.)
        - observation: specific details

        # task_list
        - task_id: auto
        - task_name: task name
        - task_description: short description
        - task_status: initial status
        - assignee: person assigned
        - due_date: due date
        - priority: priority level

        # team_members
        - member_id: auto
        - gardener_name: name of gardener

        # plant_tracker
        - plant_id: auto
        - species: type of plant
        - location: location on farm
        - planting_date: date of planting
        - health_status: general health (healthy, diseased, etc.)
        - stage: growth stage (planted, germinated, flowering, etc.)
        - notes: any special observations or needs

        # harvest_tracker
        - harvest_id: auto
        - plant_name: related plant
        - harvest_date: date of harvest
        - quantity: amount harvested
        - unit: units (kg, bunches, etc.)
        - quality: quality rating or notes, default "good"


    example:
    user input: "I harvested 5kg of tomatoes today"
    output: "add to harvest_tracker table:
        plant_name: tomatoes, 
        harvest_date: today's date,
        quantity: 5,
        unit: kg,
        quality: good"
    
    Here is the user input:
    {user_input}
    """
sqlbot_instructions = """
    Given an input question, 
    1. make sure you have all relevant information from the user, ask them for what you need before running any query.
    2. create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
    
    Use the following format:

    Request: {query_request} \n
    SQLQuery: SQL Query to run \n
    SQLResult: Result of the SQLQuery \n
    Answer: Final answer here \n
    """
