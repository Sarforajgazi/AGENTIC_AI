"""
Basic Agent
=============================

Basic Agent Quickstart.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv
load_dotenv()


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------
def build_agent():
    return Agent(
        name="Quickstart Agent",
        #model=Groq(id="openai/gpt-oss-120b"),
        model=OpenAIResponses(id="gpt-5.2"),
        tools= [
            DuckDuckGoTools()
        ],
        instructions="""
             You are a helpful assistant.
        """,
        markdown= True,
        add_datetime_to_context= True
    )


# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------

openai_agent = build_agent()
#groq_agent = build_agent()

#openai_agent.print_response("My budget is 1 Lac ruppees INR. Should i go to shimla or Kashmir?")
#groq_agent.print_response("My budget is 1 Lac ruppees INR. Should i go to shimla or Kashmir?")

#openai_agent.print_response("What is your knowledge cutoff?")

openai_agent.print_response("Is it safe to travel to UAE today?")
