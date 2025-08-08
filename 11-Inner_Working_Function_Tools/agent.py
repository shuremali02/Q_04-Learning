from agents import Agent
from tools import get_weather , search_product, send_email , schedule_meeting, find_restaurant



FunctionToolAgent = Agent(
    name="Function Tools Agent",
    instructions=(
        "You are an intelligent agent designed to understand natural language prompts "
        "and use the correct function tool based on the user's intent. "
        "Carefully extract arguments and match them with the correct tool. "
        "Always return the final result clearly and completely."
    ),
    tools=[
        get_weather,
        find_restaurant,
        send_email,
        schedule_meeting,
        search_product,
    ]
)