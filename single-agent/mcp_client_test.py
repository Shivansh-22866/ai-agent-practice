import os
import asyncio
import certifi
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": f"https://mcp.tavily.com/mcp?tavilyApiKey={TAVILY_API_KEY}",
        }
    }
)

async def get_all_tools():
    tools = await client.get_tools()
    return tools
    # for tool in tools:
    #     print(f"Tool Name: {tool.name}, Tool Description: {tool.description}")

tavily_search_tool = None

async def get_tavily_search_tool():
    global tavily_search_tool
    if tavily_search_tool is None:
        tools = await get_all_tools()
        tavily_search_tool = next((tool for tool in tools if tool.name == "tavily_search"))
    return tavily_search_tool

async def tavily_mcp_search(query: str):
    await get_tavily_search_tool()
    result = await tavily_search_tool.ainvoke(
        {"query": query}
    )
    print(f"Query: {query}\nResult: {result}")
    return result