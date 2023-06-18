from dotenv import load_dotenv, find_dotenv
import os
import gradio as gr
from modules.reasoning.component import create_reasoning_router_ui
from modules.knowledge_retrieval.component import create_knowledge_router_ui
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
        
    interface.queue()
    interface.launch()

if __name__ == "__main__":
    create_interface()
