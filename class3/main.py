from agents import Runner, set_tracing_disabled
from my_agent.gemini_agent import gemini_agent

set_tracing_disabled(True)
# user_input = "What is the result of 4+5, 10-5, 3*3 and 20/5?"



res = Runner.run_sync(
    starting_agent = gemini_agent,
    input="Get me the user data for user id 3,4 and 5",
    
    
)



# res = Runner.run_sync(starting_agent=gemini_agent, input="4+5=?")
# res = Runner.run_sync(starting_agent=gemini_agent, input="10-5=?")
# res = Runner.run_sync(starting_agent=gemini_agent, input="3*3=?")
# res = Runner.run_sync(starting_agent=gemini_agent, input="20/5=?")
print(res.final_output)