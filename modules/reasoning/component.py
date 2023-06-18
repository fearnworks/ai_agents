from modules.reasoning.reasoning_router import ReasoningRouter, get_reasoning_router_config
from modules.settings.user_settings import UserSettings
import gradio as gr


def determine_and_execute(question, temperature):
    settings = UserSettings.get_instance()
    api_key = settings.get_api_key()
    config = get_reasoning_router_config(temperature=temperature)
    config.temperature = temperature
    determiner = ReasoningRouter(api_key=api_key, config=config, question=question, display=print)
    determine_output, execute_output = determiner.determine_and_execute()
    return determine_output, execute_output

examples = [["""Bob is in the living room.
He walks to the kitchen, carrying a cup.
He puts a ball in the cup and carries the cup to the bedroom.
He turns the cup upside down, then walks to the garden.
He puts the cup down in the garden, then walks to the garage.
Where is the ball?""", 0.6], ["Given the task of building a house in the middle of a river, what are three strategies I could use to mitigate risk of flooding?", 0.6 ]]

def create_reasoning_router_ui(cache_examples=False): 
    with gr.Row():

        question = gr.Textbox(label="Enter your question here:")
        temperature = gr.Slider(minimum=0, maximum=2, default=.7, label="Temperature")
    with gr.Column():
        reasoning_strategy = gr.Textbox(label="Reasoning Strategy")
        reasoning = gr.Textbox(label="Reasoning")
    
    generate_button = gr.Button(label="Generate")
    generate_button.click(determine_and_execute, outputs=[reasoning_strategy, reasoning], inputs=[question, temperature])
    gr.Examples(examples=examples, fn=determine_and_execute, cache_examples=cache_examples, inputs=[question, temperature], outputs=[reasoning_strategy, reasoning])

