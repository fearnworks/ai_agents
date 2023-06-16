from langchain import PromptTemplate, LLMChain
import streamlit as st
from .reasoning_strategy import ReasoningStrategy, ReasoningConfig
from typing import Callable

class ChainOfThoughtStrategy(ReasoningStrategy):
    def __init__(self, config: ReasoningConfig, display: Callable):
        super().__init__(config=config, display=display)

    def run(self, question):
        print('Using Chain of Thought')
        self.display("Using 'Chain of Thought'")

        template_cot = """You are asked a question and rather than simply guessing the right answer break down the solution into a series of staps
        The question is {question}

        Write out your step by step reasoning and after considering all of the facts and applying this reasoning write out your final answer
        """
        prompt = PromptTemplate(template=template_cot, input_variables=["question"])
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        response_cot = llm_chain.run(question)
        print(response_cot)
        self.display(response_cot)

def default_cot_confg():
    usage = """
    This problem is simple and the solution may be obtained by focusing on generating a coherent series 
    of reasoning steps that lead to the final answer. The approach provides interpretability, decomposes 
    multi-step problems into intermediate steps, and allows for additional computation allocation
    """
    return ReasoningConfig(usage=usage)