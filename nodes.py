from dotenv import load_dotenv
import os
from langgraph.graph import MessagesState
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI 
from langgraph.prebuilt import ToolNode
from react import llm, tools


load_dotenv()

SYSTEM_MESSAGE = """you are a helpful assistant that can use tools to answer questions."""

def run_agent_reasoning(state:MessagesState) -> MessagesState:
    """Run the agent reasoning."""

    response = llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": [response]}

tool_node = ToolNode(tools)