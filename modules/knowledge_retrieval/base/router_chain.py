from modules.base.chain import IChain
from typing import Dict , Any, Callable
import os

class RouterChain(IChain):
    """
    RouterChain Class

    Design:
    The RouterChain class extends the IChain interface and provides an implementation for the run 
    method. It also introduces a new method, add_chain, for adding destination chains. The class adheres 
    to the Open/Closed Principle (OCP) as it can be extended without modifying its behavior.

    Intended Implementation:
    The RouterChain class serves as a router that selects the appropriate DestinationChain based on 
    the input. The selection logic should be implemented in the run method. The add_chain method 
    allows new DestinationChain instances to be added to the RouterChain.
    """
    template : str 
    destination_chains: Dict[int, IChain]
    display: Callable = print
    question: str
    usage: str
    llm: Any
    api_key: str = os.environ.get('OPENAI_API_KEY')

    def add_chain(self, domain: str, chain: IChain) -> None:
        self.destination_chains[domain] = chain

    def run(self, input: str) -> str:
        # Implement the logic to select the appropriate DestinationChain
        pass