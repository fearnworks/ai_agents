from langchain.llms import OpenAI
from pydantic import BaseModel
from langchain.llms.base import BaseLLM
from typing import Type, Callable
import streamlit as st
import os 



class ReasoningConfig(BaseModel):
    """
    A class representing a reasoning strategy for answering questions.

    Args:
        config (ReasoningConfig): The configuration for the reasoning strategy.
        display (Callable): A function for displaying output.

    Attributes:
        llm (BaseLLM): The language model used for reasoning.
        display (Callable): The function for displaying output.
    """
    temperature: float = 0.7
    max_tokens: int = 1500
    llm_class: Type[BaseLLM] = OpenAI
    usage: str

class ReasoningStrategy:
    def __init__(self, config: ReasoningConfig, display: Callable):
        self.llm = config.llm_class(temperature=config.temperature, max_tokens=config.max_tokens) # ign
        self.display = display
        self.usage = config.usage
    def run(self, question):
        raise NotImplementedError()
    
def default_reasoning_config():
    usage = "This is the default reasoning model that should only be used as a last resort"
    return ReasoningConfig(usage=usage)