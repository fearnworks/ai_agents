# AI Agents
A collection of patterns for experimenting with agents, llm pipelines, and ChainOfThoughtStrategy. 
Heavily inspired by examples and code across the AI Open Source community but with some fearnworks patterns heavily interspersed. 

## UI
Front end for templates currently uses streamlit, however display for each agent example will be heavily decoupled from deployment avenue. 
Strategies for jupyter, gradio, and react will be prioritized in general at this time. 

## Modules

### Reasoning 

General problem solving requiring reasoned processing. Utilizing tree of thoughts, chain of thought, and reAct. Current prompts heavily inspired by
work from https://github.com/mrspiggot

### Knowledge Domains

Example of knowledge domain retrieval. Given a question the router determines the best knowledge domain chain to use and then calls that chain to handle the response.

Includes examples of queries that will return each of the four implemented domains. 

### Generative Image Prompting Patterns

Coming soon 

### Generative Simulacra Pattern

Coming soon

### Story Telling / Dungeon Master Patterns

Coming Soon 

### Deployment

Project is packaged with a dockerfile expose a gradio ui on localhost:7000. Please use the envtemplate file to create your .env for running the project

To build & run

```
docker build . -t ai_agent:latest
docker run -it -p 7000:7000 ai_agent:latest
```

To build, run, and, clean up image in one command :

```
docker build . -t ai_agent:latest && docker run --rm -it -p 7000:7000 --name ai_agent_container ai_agent:latest
```