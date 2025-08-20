from agents import Runner, set_tracing_disabled
from my_agent.groq_agent import groq_agent

set_tracing_disabled(True)

res = Runner.run_sync(starting_agent=groq_agent, input="Explain the history os Pakistan in simple terms.")

print(res.final_output)