import os
from mcp.server.fastmcp import FastMCP
from zerodha_adapter import ZerodhaAdapter
from dotenv import load_dotenv

load_dotenv() 


# Create an MCP server
mcp = FastMCP("Trade-MCP")


API_KEY = os.getenv('API_KEY')
API_SECRET = os.get_env('API_SECRET')
zerodha = ZerodhaAdapter(API_KEY, API_SECRET)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def place_zerodha_buy_order(symbol: str, quantity: int) -> str:
    """Places an order using the Zerodha Broker"""
    try:
        order_id = zerodha.place_order(symbol, quantity, "BUY")
        return f"Success! Order ID: {order_id}"
    except Exception as e:
        return f"Error: {e}"


@mcp.tool()
def place_zerodha_sell_order(symbol: str, quantity: int) -> str:
    """Places an order using the Zerodha Broker"""
    try:
        order_id = zerodha.place_order(symbol, quantity, "SELL")
        return f"Success! Order ID: {order_id}"
    except Exception as e:
        return f"Error: {e}"
    
@mcp.tool()
def get_zerodha_holdings():
    """Get all the holdings in Zerodha"""
    try:
        holdings = zerodha.get_holdings()
        return holdings
    except Exception as e:
        return f"Error: {e}"

# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"