from archestra import Agent
from agent.tools.gfg_tool import gfg_tool
from agent.tools.quiz_tool import quiz_tool
from agent.tools.roadmap_tool import roadmap_tool

agent = Agent(
    name="Adaptive MCP Learning Agent",
    instructions="""
You are an adaptive learning agent.

Use tools when needed:
- Use gfg_search to fetch study materials
- Use generate_roadmap for roadmap
- Use generate_quiz for quizzes
""",
    tools=[gfg_tool, roadmap_tool, quiz_tool],
)
