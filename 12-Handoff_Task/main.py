from agents import Agent ,Runner ,trace
from dotenv import load_dotenv
from connection import config
import asyncio 
from hand_off import lyric_agent , narrative_agent , dramatic_agent



load_dotenv()



async def main():
    parent_agent=Agent(
        name="ParentAgent",
        instructions="""You are an orchestrate agent, you will be given a user input which has some stanzas then you need to find what style of the poem is it like lyric, narrative (Descriptive) or dramatic.
        then you will handoff the task to the respective agent based on the style of the poem.
        then you will return the final output in the format of the OutputFormat class.
        Remember, do not write a poem by yourself, you will handoff the task to the respective agent based on the style of the poem.""",
        handoffs=[lyric_agent , narrative_agent , dramatic_agent],
    
        

    )
    with trace("Poetry Analys"):
        runner= await Runner.run(starting_agent=parent_agent,
                                input="""Tu kaun hai jo har subah mujhe ghoorta hai?  
                                Kya tu wohi hai jo kabhi khwabon mein muskaraata tha?

                                Jawab de! Kya tu bhi jhooth bolta hai jaise baaqi sab?  
                                Ya sirf mein hi badal gaya hoon, bina bataaye? """, 
                                run_config=config)
        print(runner.final_output)
        print("Handoffs: ",runner.last_agent.name )


asyncio.run(main())

# def main():
#     print("Hello from 12-handoff-task!")


# if __name__ == "__main__":
#     main()
