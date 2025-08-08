from dotenv import load_dotenv
from connection import config
import asyncio 
import rich 
from pydantic import BaseModel
from agents import (Agent ,Runner ,
    trace,input_guardrail ,
    RunContextWrapper,
    TResponseInputItem,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered)



load_dotenv()


# Exercise # 1 Objective: Make a agent and make an input guardrail trigger. Prompt: I want to change my class timings 😭😭 Outcome: After running the above prompt an InputGuardRailTripwireTriggered in except should be called. See the outcome in LOGS



class TeacherResponse(BaseModel):
    input:str
    response:str
    isSlotChange:bool


teacher_guard_Agent=Agent(
    name="TeacherGuardrailAgent",
    instructions="""you are my teacher sir ali jawwad, your task is to check user guery is related to slot/ time/ class change or not """,
    output_type=TeacherResponse

)

@input_guardrail
async def teacher_guardrail(ctx:RunContextWrapper,
                           agent:Agent,input:TResponseInputItem):
    result= await Runner.run(teacher_guard_Agent,input,run_config=config)
    rich.print(result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isSlotChange
    )

student_agent=Agent(
    name="studentagent",
    instructions="""you are a student """,
    input_guardrails=[teacher_guardrail]
)

async def main():
    try:     
            with trace("TeacherAgent"):
                runner= await Runner.run(
                student_agent,
                """I want to change my slot """,
                run_config=config,) 
                rich.print(runner.final_output)
    except InputGuardrailTripwireTriggered:
           print("This Action is not allowed")


asyncio.run(main())        