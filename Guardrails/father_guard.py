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


# Exercise # 2 Objective: Make a father agent and father guardrail. The father stopping his child to run below 26C.


class FatherResponse(BaseModel):
    input:str
    response:str
    isTempBelow26c:bool


father_guard_Agent=Agent(
    name="FatherGuardrailAgent",
    instructions="""you'r a father Your task is to check if the user query is related to AC temperature or not. if it is then check if the temperature is below 26C or not """,
    output_type=FatherResponse

)

@input_guardrail
async def father_guardrail(ctx:RunContextWrapper,
                           agent:Agent,input:TResponseInputItem):
    result= await Runner.run(father_guard_Agent,input,run_config=config)
    rich.print(result.final_output)
    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isTempBelow26c
    )

son_agent=Agent(
    name="SonAgent",
    instructions="""you are a son """,
    input_guardrails=[father_guardrail]
)

async def main():
    try:     
            with trace("FatherAgent"):
                runner= await Runner.run(
                son_agent,
                """The AC is on 16C""",
                run_config=config,) 
                rich.print(runner.final_output)
    except InputGuardrailTripwireTriggered:
           print("This action is not allowed, You can not run below 26C")


asyncio.run(main())        


# output: 
#     FatherResponse(
#     input='The AC is on 16C',
#     response="16C? That's too cold! Are you trying to freeze us? Please turn it up to 
# at least 26C, son. We don't want to waste electricity and catch a cold.",
#     isTempBelow26c=True
# )
# This action is not allowed, You can not run below 26C