from agents import Runner, set_tracing_disabled
from my_agents.gemini_agent import agent

set_tracing_disabled(True)

res = Runner.run_sync(starting_agent=agent, input="4+4=?")

print(res.final_output)