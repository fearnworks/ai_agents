from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
from reasoning import ReasoningRouter, get_reasoning_router_config
load_dotenv(find_dotenv())


def run_app():
    """
    Runs the Streamlit application.

    Returns:
        None
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.text("AI Agents Sandbox")
    with col2:
        st.title("Prompt Strategy Demo")
    question = st.text_area('Enter your question here:', height=200)
    config = get_reasoning_router_config()
    if question:
        determiner = ReasoningRouter(api_key=openai_api_key, config=config, question=question,display=st.write)
        determiner.determine_and_execute()

if __name__ == "__main__":
    run_app()

