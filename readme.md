Agentic AI Demo: Autonomous Financial Report Generator

This is a simple demonstration of an Agentic AI system using the Agno SDK, powered by Google Gemini 2.0 Flash or OpenAI GPT-4o.

The agent autonomously gathers, reasons, and generates a real-time financial report (e.g., for NVDA) using live market data and built-in tools — showcasing the power of Agent + Tools + Reasoning.

What's Agentic AI?

Agentic AI refers to systems where AI models are equipped with tools, memory, reasoning, and autonomy — allowing them to take actions, perform multi-step thinking, and generate goal-driven outputs.

In this demo, our agent:

* Thinks (using reasoning tools)
* Acts (via finance tools like Yahoo Finance)
* Reports (clean, markdown-based outputs)

Features

* Live data via Yahoo Finance tools
* Built-in reasoning capabilities
* Stock analysis with analyst opinions, price, and news
* Gemini or GPT-4o as the foundation model
* Markdown-enabled structured output

Tech Stack

* Python
* Agno SDK for agent orchestration
* Gemini 2.0 Flash / OpenAI GPT-4o
* YFinanceTools, ReasoningTools
* .env for API key management

How to Run

1. Clone this repo
   git clone [https://github.com/your-username/agentic-ai-demo.git](https://github.com/your-username/agentic-ai-demo.git)
   cd agentic-ai-demo

2. Install dependencies
   pip install -r requirements.txt

3. Set your API keys in .env
   GEMINI\_API\_KEY=your\_google\_api\_key
   OPENAI\_API\_KEY=your\_openai\_api\_key

4. Run the agent
   python main.py

Output Example

The agent will generate a clean, table-based markdown report about the selected stock, including:

* Stock Price
* Analyst Recommendations
* Company News
* Company Info

Ideas for Expansion

* Plug into other domains (e.g., healthcare, weather, news)
* Connect to a web dashboard or mobile app
* Enable multi-agent collaboration

