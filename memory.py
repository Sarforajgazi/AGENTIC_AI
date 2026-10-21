"""
Basic Agent
=============================

Basic Agent Quickstart.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
load_dotenv()


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------
def build_agent():
    return Agent(
        name="Quickstart Agent",
        model=Groq(id="openai/gpt-oss-120b"),
        #model=OpenAIResponses(id="gpt-5.2"),
        tools= [
            DuckDuckGoTools()
        ],
        instructions="""
             You are a helpful assistant.
        """,
        markdown= True,
        db=SqliteDb(db_file="tmp/memory.db"),
        update_memory_on_run=True,
        add_history_to_context=True,
        add_datetime_to_context= True
    )



# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------

#openai_agent = build_agent()
groq_agent = build_agent()

groq_agent.print_response("What is the capital of UAE")
groq_agent.print_response("What is the best time to visit it?")