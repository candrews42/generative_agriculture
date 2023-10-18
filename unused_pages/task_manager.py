import streamlit as st
import pandas as pd
import sqlalchemy
import requests, json

# Configuration and Markdown
st.set_page_config(page_title="Task Manager", page_icon="📊")
st.markdown("# Task Manager")
st.sidebar.header("Tasks")
st.write("This demo shows database task management interactions")

# secret keys
openai_api_key = st.secrets["openai_key"]
notion_api_key = st.secrets["notion_api_key"]

# Notion API Initialization
headers = {
    "Authorization": "Bearer " + notion_api_key,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

pageID ="8fd4e70f758e4f3f88e5938cb2c0538c"

pagereadUrl = f"https://api.notion.com/v1/pages/{pageID}"
# dbreadUrl = f"https://api.notion.com/v1/databases/{databaseID}"

# Function to fetch data from Notion Database
def responseNotion(readUrl, headers):
    readUrl = readUrl
    res = requests.request("GET", readUrl, headers=headers)
    return res.json()  # Return JSON data

def notion_to_markdown(notion_data, headers):
    markdown_output = ""
    
    # Extract and format the title
    title = notion_data.get("properties", {}).get("Title", {}).get("title", [])[0].get("plain_text", "")
    markdown_output += f"# {title}\n\n"
    
    # Fetch child blocks
    block_id = notion_data.get("id")
    child_blocks = fetch_child_blocks(block_id, headers).get('results', [])
    
    # Format child blocks
    for block in child_blocks:
        block_type = block.get("type")
        text_list = block.get(block_type, {}).get("rich_text", [])  # Change here
        text_content = text_list[0].get("plain_text", "") if text_list else ""
        
        if block_type == "paragraph":
            markdown_output += f"{text_content}\n\n"
        elif block_type == "heading_1":
            markdown_output += f"# {text_content}\n\n"
        elif block_type == "heading_2":
            markdown_output += f"## {text_content}\n\n"
        elif block_type == "heading_3":
            markdown_output += f"### {text_content}\n\n"
        elif block_type == "to_do":
            checked = block.get("to_do", {}).get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            markdown_output += f"- {checkbox} {text_content}\n"
        # Handle more types as needed
    
    return markdown_output



def fetch_child_blocks(block_id, headers):
    readUrl = f"https://api.notion.com/v1/blocks/{block_id}/children"
    res = requests.request("GET", readUrl, headers=headers)
    return res.json()


st.markdown("# Notion Database Content")
# Fetch the Notion page data
page_data = responseNotion(pagereadUrl, headers)

# Convert to Markdown
markdown_content = notion_to_markdown(page_data, headers)

# Display in Streamlit
st.markdown(markdown_content)
