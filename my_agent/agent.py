from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',# Model: The reasoning engine
    name='root_agent',  # Identity: Required identifier
    description='A helpful assistant for user questions.', # Purpose: What this agent does
    instruction='Answer user questions to the best of your knowledge',  # Behavior: How to act
    # Tools: You’ll add these in the "Other ways to run your agent" module
    # Orchestration: Handled automatically by the Agent class
)
