from langchain.agents import initialize_agent, Tool, AgentExecutor
from .reasoning_strategy import ReasoningStrategy, ReasoningConfig
from langchain.docstore.wikipedia import Wikipedia
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.agents.react.base import DocstoreExplorer
from typing import Callable


class ReactStrategy(ReasoningStrategy):
    def __init__(self, config: ReasoningConfig, display: Callable):
        super().__init__(config=config, display=display)

    def run(self, question) -> str:
        print('Using ReAct')
        self.display("Using 'ReAct' - (Reasoning and Action)")

        docstore = DocstoreExplorer(Wikipedia())
        tools = [
            Tool(
                name="Search",
                func=docstore.search,
                description="Search for a term in the docstore.",
            ),
            Tool(
                name="Lookup",
                func=docstore.lookup,
                description="Lookup a term in the docstore.",
            )
        ]
        react = initialize_agent(tools, self.llm, agent="react-docstore", verbose=True)
        agent_executor = AgentExecutor.from_agent_and_tools(
            agent=react.agent,
            tools=tools,
            verbose=True,
        )
        response_react = agent_executor.run(question)
        print(response_react)
        self.display(response_react)
        return response_react

def default_react_config() -> ReasoningConfig:
    usage = """
    The solution for this problem requires searching for further information online, 
    generating reasoning traces and task-specific actions in an interleaved manner. 
    Starting with incomplete information this technique will prompt for the need to get 
    additional helpful information at each step. It allows for dynamic reasoning to create, 
    maintain, and adjust high-level plans for acting, while also interacting with external 
    sources to incorporate additional information into reasoning 
    """
    return ReasoningConfig(usage=usage)