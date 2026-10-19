from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent
import asyncio
from mcp_client_test import get_all_tools

# res = tavily_search("Cheapest flights in Bangalore")
# print(res)

# res = search_flights("Plan a 7 days Singapore trip from India")
# print(res)

# user_query = "Plan a 7 days Singapore trip from India"

# res = run_travel_agent(
#     user_input=user_query,
#     thread_id="test_thread",
# )
# print(res["answer"])

asyncio.run(get_all_tools())