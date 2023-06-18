import gradio as gr
from modules.settings.user_settings import UserSettings

def set_api_key(key: str):
    UserSettings.get_instance().set_api_key(key)
    return "API key set"


def create_settings_ui():
    settings = UserSettings.get_instance()
    api_key_default = settings.get_api_key()
    api_key = gr.Textbox(label="You OpenAI API key", type="password")
    set_status = gr.Text()
    key_button = gr.Button(label="Set Key")
    key_button.click(set_api_key, outputs=[set_status], inputs=[api_key])