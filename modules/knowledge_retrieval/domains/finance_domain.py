from modules.base.llm_chain_config import LLMChainConfig
from modules.knowledge_retrieval.destination_chain import DestinationChainStrategy
from modules.knowledge_retrieval.base import KnowledgeDomain
from loguru import logger
from langchain import PromptTemplate, LLMChain
from langchain.llms.openai import OpenAI
from typing import Callable
import pprint 

class FinanceDomain(KnowledgeDomain):
    """
    FinanceDomain Class

    Design:
    This class is a specific implementation of the KnowledgeDomain class. It provides a specific 
    implementation for generating responses to finance-related questions. Following the Single 
    Responsibility Principle (SRP), its sole responsibility is to generate finance-related responses.

    Intended Implementation:
    The generate_response method should generate appropriate responses to finance-related questions. 
    Depending on the specifics of the problem domain, this could involve a rule-based approach, 
    using a trained machine learning model, or some other method of generating responses.
    """
    def generate_response(self, question: str) -> str:
        template_cot = """You are asked a finance-related question and rather than simply guessing the right answer break down the solution into a series of steps
        The question is {question}

        Write out your step by step reasoning and after considering all of the facts and applying this reasoning write out your final answer
        """
        prompt = PromptTemplate(template=template_cot, input_variables=["question"])
        llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.7, max_tokens=1500))  # assuming OpenAI is the LLM to be used
        response_cot = llm_chain.run(question)
        return response_cot


class FinanceChain(DestinationChainStrategy):
    """
    FinanceChain Class

    Design:
    This class is a specific implementation of the ChainStrategy class.
    It follows the Open/Closed Principle (OCP) because it extends the ChainStrategy class 
    without modifying its behavior. It also adheres to the Dependency Inversion Principle (DIP) as it 
    depends on the abstraction (FinanceDomain) rather than a concrete class.

    Intended Implementation:
    The FinanceChain class serves as a wrapper around a FinanceDomain instance. It implements the run 
    method from the ChainStrategy class, which simply calls the generate_response method of the FinanceDomain.
    As such, when the run method is called with a question as input, the FinanceChain class will return a 
    response generated by the FinanceDomain.
    """
    def __init__(self, config: LLMChainConfig, display: Callable):
        super().__init__(config=config, display=display, knowledge_domain=FinanceDomain(), usage=config.usage)
        print("Creating Finance Chain with config: ")
        pprint.pprint(vars(config))

    def run(self, question):
        print('Using Finance Chain of Thought')
        self.display("Using 'Finance Chain of Thought'")
        response_cot = super().run(question)
        return response_cot

def get_finance_chain_config(temperature: float = 0.7) -> LLMChainConfig:
    usage = """
    This problem is finance-related and relates to the following topics:
    - Financial Planning
    - Financial Analysis
    - Financial Management
    - Financial Markets
    - Financial Instruments
    - Financial Services

    Or things of this nature
    """
    return LLMChainConfig(usage=usage, temperature=temperature)