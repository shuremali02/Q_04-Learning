# 🪙 Crypto Currency Agent using OpenAI Agent SDK

This is an AI-powered crypto agent built using the **OpenAI Agent SDK** and **Coinlore API**. It uses multiple tools (functions) to fetch live cryptocurrency data and respond to user queries like:

> 🔹 “Show me the top 10 coins”  
> 🔹 “What is the price of BTC?”  
> 🔹 “Give me today’s crypto market overview”  

---

## 🚀 Tech Stack

- **Python**
- **UV**
- **OpenAI Agents SDK**
- **Streamlit (Frontend)**
- **Coinlore Public API**

---

## 🧠 Available Tools (Function Handlers)

### 1. `get_all_tickers(start=0, limit=10)`
🔍 **Purpose:** Fetch top coins in the market  
📦 **Returns:** Symbol, price, market cap, volume, etc.  
🧠 **Use Case:** When user asks: *“Show me top 10 coins”*

---

### 2. `get_ticker_by_id(ticker_id)`
🔍 **Purpose:** Retrieves data for a specific coin via its ID  
🎯 **Input:** Numeric coin ID (e.g., 90 for BTC)  
🧠 **Use Case:** Used internally after fetching ID via symbol

---

### 3. `get_cryptoInfo()`
🔍 **Purpose:** Provides overall market overview  
📈 **Returns:** Total market cap, 24h volume, active currencies  
🧠 **Use Case:** User asks: *“What’s today’s crypto market overview?”*

---

### 4. `get_ticker_by_symbol(symbol)`
🔍 **Purpose:** Converts coin symbol (e.g., BTC) to its numeric ID  
🧠 **Use Case:** Used before calling `get_ticker_by_id`  

---

### 5. `get_market_cap_id(market_cap_id)`
🔍 **Purpose:** Provides market stats of a specific coin  
📦 **Returns:** Market cap-related data  

---

## 🌐 Coinlore API Endpoints Used

We are using the [Coinlore Public API](https://www.coinlore.com/cryptocurrency-data-api) for real-time data:

| Endpoint | Description |
|----------|-------------|
| `/api/tickers/?start=0&limit=10` | Fetch top coins |
| `/api/ticker/?id=90` | Coin data by ID |
| `/api/global/` | Crypto market global data |
| `/api/ticker/?id=MARKET_CAP_ID` | Market data for a coin |
| `/api/tickers/` | Used in symbol lookup logic |

---

## 🧪 How to Run

```bash
# Step 1: Clone this repo
git clone https://github.com/shuremali02/Crypto_Currency_Agent_Open_Ai_SDK.git
cd Crypto_Currency_Agent_Open_Ai_SDK

# Step 2: Install dependencies (recommended inside a virtual env)
uv add -r requirements.txt

# Step 3: Add your environment variables
touch .env
# Add GEMINI_API_KEY or any other needed API keys

# Step 4: Run the agent using Streamlit
streamlit run main.py
