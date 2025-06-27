import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

# Setup the agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=api_key),  # or use OpenAIChat(id="gpt-4o")
    tools=[
        ReasoningTools(add_instructions=True)
    ],
    instructions=[
        "You are a rural health assistant AI. Analyze given symptoms or vitals.",
        "Your goal is to provide early wellness insights and next-step suggestions.",
        "Use simple language. Include possible health risks and urgency level.",
        "If necessary, recommend visiting a health center.",
        "Only output the report. Avoid generic responses."
    ],
    markdown=True
)

# Simulated health input (this can come from form, voice, or sensor data)
user_input = """
Patient is experiencing:
- persistent headache
- mild fever
- dizziness
- fatigue
Temperature: 99.8°F
Pulse: 92 bpm
Age: 52
Gender: Female
"""

# Generate the health report
agent.print_response(
    message=f"Generate a wellness report based on the following data:\n{user_input}",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=False
)
