import aiohttp
import os
from fastmcp import FastMCP

WEATHER_API_KEY = os.getenv("WEATHERAPI_API_KEY")
# --- Configuration ---
# It's recommended to load this from an environment variable in a real application
# WEATHER_API_KEY = "YOUR_WEATHERAPI_COM_API_KEY"


# Initialize the FastMCP server
mcp = FastMCP("WeatherService")

@mcp.tool
async def get_weather(location: str) -> dict:
    """
    Fetches the current weather for a given location.

    :param location: The city and state, or zip code.
    :return: A dictionary containing the weather information.
    """
    if not WEATHER_API_KEY or WEATHER_API_KEY == "YOUR_WEATHERAPI_COM_API_KEY":
        return {"error": "Weather API key is not configured."}

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": f"Error fetching weather data: {response.status}"}

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)