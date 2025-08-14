from dotenv import load_dotenv  
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
from rich import print
import asyncio


class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

@function_tool
def get_book_info(wrapper: RunContextWrapper[LibraryBook]):
    return f"""
            The book {wrapper.context.book_title} 
            is written by {wrapper.context.author_name} 
            and is available: {wrapper.context.is_available} 
            id: {wrapper.context.book_id}
            """

agent = Agent(
    name="Library Agent",
    instructions="You are a helpful assistant, always call the tool to get book's information",
    tools=[get_book_info]
)

async def main():
    book = LibraryBook(book_id="BOOK-123", 
    book_title="Python Programming",
     author_name="John Smith", 
     is_available=True)

    result = await Runner.run(
        agent,
        "What is the book's information?",
        context=book,
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
