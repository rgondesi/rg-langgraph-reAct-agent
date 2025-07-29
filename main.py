from dotenv import load_dotenv
import os
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()

@tool
def triple(x: int) -> int:
    """Return the triple of x."""
    return 3 * x

tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    api_key=os.getenv("OPENAPI_KEY")
).bind_tools(tools)


if __name__ == "__main__":
    print("This script is intended to be imported as a module, not run directly.")
    print(os.getenv("OPENAPI_KEY", "Default Value"))