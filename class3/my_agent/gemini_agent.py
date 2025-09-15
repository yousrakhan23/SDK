from agents import Agent
from my_config.gemini_config import GEMINI_MODEL
# from my_data_type.my_data_type_schema import MyData
from my_tool.math_tools import plus, subtract, multiply, divide
from  my_tool.user_data import fetch_user_data, fetch_user_data_by_id
gemini_agent =Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant. explain in details how to solve the problem step by step.",
    model=GEMINI_MODEL,
    # output_type=MyData,
    tools=[plus, subtract, multiply, divide, fetch_user_data, fetch_user_data_by_id],
)

print(gemini_agent.name)
print(gemini_agent.tools)