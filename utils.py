import os
import random
import streamlit

# from api_keys import openai_key, postgresql_key 
mode = "local"
# mode = "cloud"

#decorator
def enable_chat_history(func):
    if os.environ.get("OPENAI_API_KEY"):

        # to clear chat history after swtching chatbot
        current_page = func.__qualname__
        if "current_page" not in streamlit.session_state:
            streamlit.session_state["current_page"] = current_page
        if streamlit.session_state["current_page"] != current_page:
            try:
                streamlit.cache_resource.clear()
                del streamlit.session_state["current_page"]
                del streamlit.session_state["messages"]
            except:
                pass

        # to show chat history on ui
        if "messages" not in streamlit.session_state:
            streamlit.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        for msg in streamlit.session_state["messages"]:
            streamlit.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    streamlit.session_state.messages.append({"role": author, "content": msg})
    streamlit.chat_message(author).write(msg)

def configure_openai_api_key():
    # openai_api_key = openai_key
    # if mode == "local":
    #     openai_api_key = openai_key
    # else:
    openai_api_key = streamlit.secrets["openai_key"]
    if openai_api_key:
        streamlit.session_state['OPENAI_API_KEY'] = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key
    else:
        streamlit.error("Please add your OpenAI API key to continue.")
        streamlit.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
        streamlit.stop()
    return openai_api_key