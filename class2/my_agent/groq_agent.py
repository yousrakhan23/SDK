from agents import Agent
from my_config.groq_config import GROQ_MODEL

groq_agent =Agent(
    name="Groq Agent",
    instructions="You are a helpful assistant.explain in details.",
    model=GROQ_MODEL,
)