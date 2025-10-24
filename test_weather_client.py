import asyncio
from fastmcp.client import Client

async def main():
    """
    An asynchronous function to connect to the MCP server and test the get_weather tool.
    """
    # The URL should point to your running MCP server
    async with Client("http://127.0.0.1:8000/mcp") as client:
        
        print("Fetching weather for New York...")

        # CORRECT WAY to call a tool:
        # Use client.call_tool("tool_name", {"param_name": "value"})
        result = await client.call_tool("get_weather", {"location": "New York"})
        
        print("\n--- Weather Data ---")
        print(result)
        print("--------------------")

        print("\nFetching weather for London...")
        result_london = await client.call_tool("get_weather", {"location": "London"})

        print("\n--- Weather Data ---")
        print(result_london)
        print("--------------------")

if __name__ == "__main__":
    asyncio.run(main())