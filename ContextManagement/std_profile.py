from dotenv import load_dotenv  
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
from rich import print
import asyncio


load_dotenv()

class StudentProfile(BaseModel):
   student_id:str
   student_name:str
   current_semester:int
   total_courses:int

@function_tool 
def get_student_profile(wrapper: RunContextWrapper[StudentProfile]):
    return f"""
    This is Student Profile
    Student ID: {wrapper.context.student_id}
    Student Name: {wrapper.context.student_name}
    Current Semester: {wrapper.context.current_semester}
    Total Courses: {wrapper.context.total_courses}
    """

agent = Agent(
    name="Student Agent",
    instructions="You are a helpful assistant, always call the tool to get student's information",
    tools=[get_student_profile]
)

async def main():
    student_profile = StudentProfile(student_id="123", student_name="ALi", current_semester=3, total_courses=3)

    result = await Runner.run(
        agent,
        "What is the student's profile?",
        context=student_profile,
        run_config=config
    )

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
