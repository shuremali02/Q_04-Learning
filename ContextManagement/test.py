from pydantic import BaseModel
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool,RunConfig, RunContextWrapper
from dotenv import load_dotenv
import os
import asyncio
from connection import config

load_dotenv()


class UserInfo(BaseModel):
    name: str
    age: int



@function_tool
def get_user_info(ctx: RunContextWrapper[UserInfo]):
    """Fetch the user details"""
    return f"The name of user is {ctx.context.name} and age is {ctx.context.age}"


sub_agent = Agent(
    name="Sub Agent",
    instructions="You are a sub-agent who can access the user's name and age using tools.if tool is not available then polietly say sorry to user",
    tools=[get_user_info]
    

)

main_agent = Agent(
    name="Main Agent",
    instructions="you are a sub-agent who can access the user's name and age using tools.",
    tools=[get_user_info],
    handoffs=[sub_agent]
)


user = UserInfo(name="Muhammad Ali", age=30)

result = Runner.run_sync(
    starting_agent=main_agent,
    input="What is user name and age? tell me this using sub agent",
    context=user,
    run_config=config
)

print(result.final_output)