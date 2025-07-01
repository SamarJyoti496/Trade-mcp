# Trade-MCP

A modular trading automation project using Zerodha Kite Connect and MCP (Modular Command Platform) for tool-based and resource-based automation. This project exposes trading actions (like placing orders and fetching holdings) as MCP tools, making them accessible to Claude Desktop and other MCP-compatible clients.

---

## Features

- **Zerodha Integration:** Place buy/sell orders and fetch holdings using the Kite Connect API.
- **MCP Tools:** Expose trading actions as callable tools for automation and AI agents.
- **Environment-based Secrets:** API keys and secrets are loaded from a `.env` file for security.
- **Extensible:** Easily add new tools or resources for more trading actions.

---

## Setup

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd Trade-MCP
```

### 2. Create and Activate a Virtual Environment

```sh
uv venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On Linux/Mac
```

### 3. Install Dependencies

```sh
uv pip install -r requirements.txt
# or, if using pyproject.toml:
uv pip install .
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
API_KEY=your_zerodha_api_key
API_SECRET=your_zerodha_api_secret
```

### 5. Get Your Zerodha Access Token

To use the Zerodha API, you need an **access token**. Follow these steps:

1. **Get Your API Key and Secret**

   - Obtain these from the [Zerodha developer console](https://developers.kite.trade/apps).

2. **Generate the Login URL**  
   In a Python shell or script, run:

   ```python
   from kiteconnect import KiteConnect
   kite = KiteConnect(api_key="your_api_key")
   print(kite.login_url())
   ```

   - Open the printed URL in your browser and log in with your Zerodha credentials.

3. **Extract the `request_token`**

   - After login, you will be redirected to your redirect URL (set in the Zerodha app settings).
   - The URL will look like:  
     `http://localhost:8000/?request_token=REQUEST_TOKEN_HERE&action=login&status=success`
   - Copy the `request_token` value from the URL.

4. **Exchange the `request_token` for an `access_token`**  
   In a Python shell or script, run:

   ```python
   data = kite.generate_session("REQUEST_TOKEN_HERE", api_secret="your_api_secret")
   print(data["access_token"])
   ```

   - Replace `"REQUEST_TOKEN_HERE"` and `"your_api_secret"` with your actual values.
   - The printed value is your `access_token`.

5. **Set the Access Token**
   - You can set this as an environment variable or use it directly in your code as needed.

---

## Usage

### Run the MCP Server

```sh
uv run --with mcp[cli] mcp run server.py
```

Or, if MCP CLI is installed in your environment:

```sh
mcp run server.py
```

### Claude Desktop Integration

1. Add a server entry in your `claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "Trade-MCP": {
         "command": "uv.EXE", # Exact Path to uv executable
         "args": [
           "run",
           "--with",
           "mcp[cli]",
           "mcp",
           "run",
           "server.py" # Exact Path to your server script
         ]
       }
     }
   }
   ```

2. Restart Claude Desktop.

3. The tools will appear in Claude's tool list.

---

## Exposed Tools

- `add(a: int, b: int)`: Add two numbers.
- `place_zerodha_buy_order(symbol: str, quantity: int)`: Place a buy order.
- `place_zerodha_sell_order(symbol: str, quantity: int)`: Place a sell order.
- `get_zerodha_holdings()`: Get all holdings from Zerodha.

---

## Extending

To add a new tool, define a function in `server.py` and decorate it with `@mcp.tool()`:

```python
@mcp.tool()
def my_tool(...):
    ...
```

---

## License

MIT License

---
