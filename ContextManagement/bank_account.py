from dotenv import load_dotenv  
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
from rich import print
import asyncio

load_dotenv()

class BankAccount(BaseModel):
    account_number: str
    balance: float
    account_holder_name: str
    is_active: bool

@function_tool
def get_bank_account_info(wrapper: RunContextWrapper[BankAccount]):
    return f"""The bank account {wrapper.context.account_number} 
            is held by {wrapper.context.account_holder_name} 
            and has a balance of {wrapper.context.balance} 
            and is active: {wrapper.context.is_active}"""   

agent = Agent(
    name="Bank Account Agent",
    instructions="You are a helpful assistant, always call the tool to get bank account information",
    tools=[get_bank_account_info]
)

async def main():
    bank_account = BankAccount(account_number="123456789", balance=100000000.0, account_holder_name="Ali", is_active=True)

    result = await Runner.run(
        agent,
        "What is the bank account information?",
        context=bank_account,
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
