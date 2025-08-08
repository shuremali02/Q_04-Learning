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


# Exercise # 3 Objective: Make a gate keeper agent and gate keeper guardrail. The gate keeper stopping students of other school.


class GateKeeperResponse(BaseModel):
    input:str
    response:str
    isSchoolStd:bool


gate_keeper_guard_Agent=Agent(
    name="GareKeeperGuardrailAgent",
    instructions="""Your school name is DubaiSchool. Your task is to check if the user query is related to student of other school entering in your school or not." """,
    output_type=GateKeeperResponse

)

@input_guardrail
async def gate_keeper_guardrail(ctx:RunContextWrapper,
                           agent:Agent,input:TResponseInputItem):
    result= await Runner.run(gate_keeper_guard_Agent,input,run_config=config)
    rich.print(result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isSchoolStd
    )

student_agent=Agent(
    name="studentagent",
    instructions="""you are a student """,
    input_guardrails=[gate_keeper_guardrail]
)

async def main():
    try:     
            with trace("GateKeeperAgent"):
                runner= await Runner.run(
                student_agent,
                """""",
                run_config=config,) 
                rich.print(runner.final_output)
    except InputGuardrailTripwireTriggered:
           print("You are not allowed to enter in DubaiSChool")


asyncio.run(main())       


# querry: i'm ali for ABCschool 
# TripwireTriggered: True
# output: 
# GateKeeperResponse(
#     input="i'm ali for ABCschool",
#     response='Yes, this query is about a student from another school entering         
# DubaiSchool.',
#     isSchoolStd=True
# )