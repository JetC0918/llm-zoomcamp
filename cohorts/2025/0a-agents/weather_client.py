# weather_client.py
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:8001/mcp/") as mcp_client:
        result1 = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print(f"Berlin: {result1}°C")

        result2 = await mcp_client.call_tool("set_weather", {"city": "Germany", "temp": 25.0})
        print(f"Set Germany weather: {result2}")

        result3 = await mcp_client.call_tool("get_weather", {"city": "Germany"})
        print(f"Germany: {result3}°C")

if __name__ == "__main__":
    asyncio.run(main())
