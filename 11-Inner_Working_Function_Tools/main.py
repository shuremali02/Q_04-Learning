import asyncio
from agents import Runner
from agent import FunctionToolAgent
from connection import config  

prompts = [
    "What's the weather going to be like in Dubai tomorrow afternoon?",
    "Find me some good Chinese restaurants near downtown that are open right now",
    "Send an email to Sarah about the project deadline being moved to next Wednesday",
    "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign",
    "I want to buy a wireless Bluetooth headphones under $100 with good reviews"
]

async def main():
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        runner = await Runner.run(FunctionToolAgent, input=prompt, run_config=config)
        print("\n✅ Final Output:", runner.final_output)

        import json
        print("\n🔎 Raw Response Dump:")
        print(json.dumps(runner.raw_responses, indent=2))



if __name__ == "__main__":
    asyncio.run(main())
