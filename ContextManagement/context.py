
# import asyncio
from pydantic import BaseModel
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool, trace

# Context data model
class UserInfo(BaseModel):
    name: str
    id: int



@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]):
    """Fetch the age of the user. Call this function to get user's age information."""
    return f"The user {wrapper.context.name} is 47 years old"
async def main():
    user_info = UserInfo(name="John", id=123)

    agent = Agent[UserInfo](
        name="Assistant",
        instructions="You are a helpful assistant.",
        tools=[fetch_user_age],
    )

    async with trace("ContextManagement"):
        result = await Runner.run(
            starting_agent=agent,
            input="What is the age of the user?",
            context=user_info,
            run_config=config,
        )

    print(result.final_output)  # The user John is 47 years old.

if __name__ == "__main__":
    asyncio.run(main())
