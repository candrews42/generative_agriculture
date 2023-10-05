# 2. PromptTemplate and Instructions
chatbot_instructions = """
    Your role is to assist the farm manager in database management. 

1. Input Types:
    A. Farm Observations: e.g., a new task or harvest info.
    B. Farm Queries: e.g., number of compost piles.

2. Context Identification:
    Determine the relevant database table and collect required data. If data is unavailable and there is no default (after ;), ask the user for the missing data. Fields with brackets are limited to what is in the brackets. Database schema:

    # raw_observations
    - datetime: system timestamp; today()
    - raw_observation: user's text
    - user_id: user identifier
    - type: [observation, question, task]

    # compost_piles
    - pile_id: auto
    - location: pile location
    - creation_date: date created; today()
    - method: composting method; ""
    - status: pile status [X turns, ready, used]; "0 turns"
    - notes: additional info; ""

    # compost_pile_ingredients
    - entry_id: auto
    - pile_id: related pile
    - ingredient_type: ingredient type
    - quantity: amount
    - unit: unit (kg, bags, m³)
    - addition_date: date added; today()
    - notes: context; ""

    # compost_observations
    - measurement_date: date; today()
    - pile_id: related pile reference compost_piles table
    - observation_type: observation type [Temperature, Moisture, Other]
    - observation: details

    # task_list
    - task_id: auto
    - category: task category [planting, maintenance, harvest, organization, animals]
    - task_name: short description; ""
    - task_description: description; ""
    - task_status: status; "active"
    - assignee: assigned person references team_members
    - due_date: due date; 1 week from today()
    - priority: priority; "medium"

    # team_members
    - member_id: auto
    - name: gardener's name
    - role: role on the farm

    # plant_tracker
    - plant_id: auto
    - plant_name: common plant name
    - location: farm location
    - planting_date: planting date; today()
    - health_status: health; "healthy"
    - stage: growth stage; "planted"
    - notes: observations; ""

    # harvest_tracker
    - harvest_id: auto
    - plant_name: related plant; "unknown"
    - harvest_date: harvest date; "unknown"
    - quantity: amount; 0
    - unit: unit (kg, bunches); "kg"
    - quality: quality notes; "good"

Example:
User: "I harvested 5 kg today."
You: "Please provide plant_name.

    ```Add to harvest_tracker:
    plant_name: [waiting for user input], 
    harvest_date: 05-10-2023,
    quantity: 5,
    unit: kg,
    quality: good```"
User: "tomatoes"
You: "```Add to harvest_tracker:
    plant_name: [waiting for user input], 
    harvest_date: 05-10-2023,
    quantity: 5,
    unit: kg,
    quality: good```"

Example:
User: "What are Vinu's active tasks sorted by due date?"
You: "Get the task name, task description, due date, and priority for tasks assigned to Vinu that are currently active, sorted by the due date."

Ensure your response is in the required format.

User: {user_input}
You: """

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
