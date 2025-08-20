from agents import Agent
from my_config.gemini_config import MODEL

agent =Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant. explain in details how to solve the problem step by step.",
    model=MODEL,
)