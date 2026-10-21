"""
Basic Agent
=============================

Basic Agent Quickstart.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team

from dotenv import load_dotenv
load_dotenv()


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

eng_agent= Agent(name="English Agent", role="you answer question in english")
chi_agent = Agent(name="Chinese Agent", role="you answer question in chinese")
hindi_agent = Agent(name="Hindi Agent", role="you answer question in hindi")

team_leader = Team(
    name="Translation Team",
    members=[
        eng_agent,
        chi_agent,
        hindi_agent
    ],
    model = Groq(id="qwen/qwen3.8-27b"),
    markdown=True,
    instructions=""" For every user input, invoke all three agents: the English Translation Agent, the Chinese Translation Agent, and the Hindi Translation Agent. 
    Each agent must independently process the original user input and return its translation in its assigned language. Do not select only one agent or return a single best response.
    Collect all three agents' outputs and combine them into one final response, clearly labeled English, Chinese (Simplified), and Hindi.
    Ensure all three agents participate in every request, and never omit an agent's response unless it fails, in which case report the failure explicitly."""

)

# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------

team_leader.print_response("What is the capital of India?")

