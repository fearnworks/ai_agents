from loguru import logger
from pydantic import BaseModel

class IChain(BaseModel):
    """
    IChain Class (Interface for Chain)

    Design:
    This class is an interface that defines the basic structure for a chain class. It's not intended to be 
    instantiated directly, but should be extended by other classes that implement the run method. This follows 
    the Interface Segregation Principle (ISP), as it provides a simple, specific interface for chain classes.

    Intended Implementation:
    Classes that extend IChain should provide an implementation for the run method. The run method should take 
    a string input and return a string output. The specifics of what the run method does will depend on the 
    requirements of the subclass.
    """
    def run(self, input: str) -> str:
        logger.info("Running IChain with input: {}", input)
        pass

