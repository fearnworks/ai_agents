import argparse
from dotenv import load_dotenv, find_dotenv
import os
import gradio as gr
from modules.reasoning.component import create_reasoning_router_ui
from modules.knowledge_retrieval.component import create_knowledge_router_ui
from modules.settings.component import create_settings_ui
from modules.settings.user_settings import UserSettings
load_dotenv(find_dotenv())

openai_api_key = os.getenv("OPENAI_API_KEY")

def create_interface():
    title: str = "Prompt Strategy Demo"
    description: str = "AI Agents Sandbox"
    with gr.Blocks(analytics_enabled=False, capture_session=True, title=title) as interface:
        with gr.Tab("Reasoning Router"):
            create_reasoning_router_ui()
        with gr.Tab("Knowledge Domains"):
            create_knowledge_router_ui()
        with gr.Tab("Settings"):
            create_settings_ui()
        
    interface.queue()
    interface.launch(server_name="0.0.0.0", server_port=port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, help="Port number to run the server on")
    args = parser.parse_args()

    port = args.port
    settings = UserSettings().get_instance()
    if openai_api_key:
        settings.set_api_key(openai_api_key)
    create_interface()