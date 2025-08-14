import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich

class UserInfo(BaseModel):
    user_id: int | str
    name: str
user = UserInfo(user_id= 2222, name="Syed Shurem ALi")

@function_tool
def get_user_info(wrapper: RunContextWrapper[UserInfo]):
    return f'The user info is {wrapper.context.name} and user id is {wrapper.context.user_id}'
personal_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get user's information",
    tools=[get_user_info]
)

async def main():
    result = await Runner.run(
        personal_agent, 
        # 'What is the user id', 
        'What is my name and user id', 
        run_config=config,
        context = user #Local context
        )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())