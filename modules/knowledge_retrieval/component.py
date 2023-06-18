from modules.knowledge_retrieval.knowledge_router import KnowledgeDomainRouter, get_knowledge_domain_router_config
import gradio as gr
import os 
openai_api_key = os.getenv("OPENAI_API_KEY")

def determine_and_execute(api_key, question: str, temperature: float):
    config = get_knowledge_domain_router_config(temperature=temperature)
    config.temperature = temperature
    determiner = KnowledgeDomainRouter(api_key=api_key, config=config, question=question, display=print)
    determine_output, execute_output = determiner.determine_and_execute(question=question)
    return determine_output, execute_output

examples = [["""When is my grandmothers birthday?""", 0.6], ["What was my tax burden last year?", 0.6 ], ["What is the most recent magic the gathering card set released?", 0.6], ["What products are the most popular with my small business customers?", 0.6]]

def create_knowledge_router_ui(cache_examples=False):  
    api_key = gr.Textbox(label="You OpenAI API key", type="password")
    with gr.Row():
        question = gr.Textbox(label="Enter your question here:")
        temperature = gr.Slider(minimum=0, maximum=2, default=.7, label="Temperature")
    with gr.Column():
        reasoning_strategy = gr.Textbox(label="Reasoning Strategy")
        reasoning = gr.Textbox(label="Reasoning")
    
    generate_button = gr.Button(label="Generate")
    generate_button.click(determine_and_execute, outputs=[reasoning_strategy, reasoning], inputs=[api_key, question, temperature])
    gr.Examples(examples=examples, fn=determine_and_execute, cache_examples=cache_examples, inputs=[question, temperature], outputs=[reasoning_strategy, reasoning])

