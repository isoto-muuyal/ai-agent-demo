from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

from app.tools.math_tools import multiply

def get_tools():
    return [
        Tool(
            name=Multiplayer,
            func=lambda x: multiply(*map(int, x.split(','))),
            description="Useful for when you need to multiply two numbers together."
        )
    ]

def create_agent():
    llm = ChatOpenAI(temperature=0)

    agent = initialize_agent(
        tools=get_tools(),
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    return agent
