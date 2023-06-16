from dotenv import load_dotenv, find_dotenv
import os
import gradio as gr
from reasoning import ReasoningRouter, get_reasoning_router_config
load_dotenv(find_dotenv())

openai_api_key = os.getenv("OPENAI_API_KEY")


def determine_and_execute(question, temperature):
    config = get_reasoning_router_config(temperature=temperature)
    config.temperature = temperature
    determiner = ReasoningRouter(api_key=openai_api_key, config=config, question=question, display=print)
    determine_output, execute_output = determiner.determine_and_execute()
    return determine_output, execute_output

iface = gr.Interface(
    fn=determine_and_execute,
    inputs=[gr.components.Textbox(label="Enter your question here:"), gr.components.Slider(minimum=0, maximum=2, default=.7, label="Temperature")],
    outputs=[gr.components.Textbox(label="Reasoning Strategy"), gr.components.Textbox(label="Reasoning")],
    title="Prompt Strategy Demo",
    description="AI Agents Sandbox"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7000)