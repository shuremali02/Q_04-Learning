# OpenAI Agents SDK Learning Project

Welcome to my **OpenAI Agents SDK Learning Project**! This project dives into the OpenAI Agents SDK, a powerful tool for building smart AI helpers. I've answered key questions about the SDK in a super simple way, so even a 10-year-old can understand! Whether you're new to coding or an experienced developer, this repo will help you learn how to create AI agents that can answer questions, solve problems, and work together like a team.

This work is part of the [Panaversity Learn Agentic AI course](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first) and draws from OpenAI’s official documentation for the [Agent Class](https://openai.github.io/openai-agents-python/ref/agent/) and [Run Method](https://openai.github.io/openai-agents-python/ref/run/). For a deeper dive, check out my detailed blog post on Medium: **[OpenAI Agents SDK: A Beginner's Guide to Building Smart AI Helpers](https://medium.com/@shuremsyed41/openai-agents-sdk-a-beginners-guide-to-building-smart-ai-helpers-understanding-openai-agents-sdk-ec8ec76cb223)**.

## Project Overview

This repository explores four key questions about the OpenAI Agents SDK, explained in a fun and easy-to-understand way. The goal is to show how the SDK can be used to build AI agents that do awesome things like answering questions or planning tasks. Below are the questions and their summaries.

## Questions and Answers

### 1. Why Is the Agent Class Defined as a Dataclass?

A **dataclass** in Python is like a toy box that neatly organizes data. The `Agent` class is a dataclass because:
- **Easy Setup**: It reduces code by automatically creating methods like `__init__` and `__repr__`.
- **Organized Data**: It keeps `instructions`, `model`, and `tools` neatly arranged.
- **Readable Code**: It makes the code shorter and easier for developers to understand.

**Example**:
```python
from dataclasses import dataclass

@dataclass
class Robot:
    name: str
    color: str
    size: int
```

### 2a. Why Is the System Prompt Stored as Instructions in the Agent Class? Why Can It Be a Callable?

The **system prompt** tells the AI how to behave (e.g., “Be a health coach”). It’s stored as `instructions` in the `Agent` class to:
- **Set a Default Role**: Defines the agent’s purpose from the start.
- **Enable Reuse**: Allows the agent to use the same instructions repeatedly.

It can be a **callable** (a function) to:
- **Dynamic Behavior**: Generate instructions based on the situation, like “Give today’s health tips.”
- **Flexibility**: Adapt to different user needs.

**Example**:
```python
def dynamic_instructions():
    return "Create a healthy diet plan for today."

@dataclass
class Agent:
    instructions: str | Callable = dynamic_instructions
```

### 2b. Why Is the User Prompt Passed as a Parameter in the Run Method, and Why Is It a Classmethod?

The **user prompt** is the question you ask the AI (e.g., “Tell me a healthy recipe”). It’s passed as a parameter in the `run` method because:
- **Changes Every Time**: User prompts vary, so they’re not stored in the `Agent` class.
- **Flexibility**: Allows asking different questions, like “What’s for breakfast?” or “What’s for dinner?”

The `run` method is a **classmethod** to:
- **Simplify Access**: Call it without creating a `Runner` object (e.g., `Runner.run()`).
- **Share Logic**: Use the same logic for all agents, reducing code duplication.

**Example**:
```python
from openai_agents import Runner

user_prompt = "Tell me a healthy recipe."
result = Runner.run(agent=health_agent, prompt=user_prompt)
```

### 3. What’s the Purpose of the Runner Class?

The `Runner` class is like a coach for the `Agent`. It:
- **Runs the Agent**: Sends instructions and user prompts to the AI model and gets answers.
- **Handles Technical Stuff**: Manages connections to the AI model, so you don’t have to.
- **Supports Flexible Workflows**: Works with one agent or multiple agents together.

**Example**: It’s like telling a robot to cook food, and the `Runner` guides it on picking ingredients and following a recipe.

### 4. What Are Generics in Python? Why Are They Used for TContext?

**Generics** in Python let you write flexible and safe code, like a magic box that can hold any data type (strings, numbers, etc.). The `typing` module (e.g., `TypeVar`) helps define these.

`TContext` is a generic type in the `Agent` or `Runner` class, acting as a placeholder for the agent’s context (e.g., user’s name or location). It’s used to:
- **Enable Flexibility**: Work with different data types for different agents.
- **Ensure Type Safety**: Catch errors if the wrong data type is used.
- **Make Code Reusable**: Use the same code in different projects with varying contexts.

**Example**:
```python
from typing import TypeVar

TContext = TypeVar("TContext")

@dataclass
class Agent:
    context: TContext
```