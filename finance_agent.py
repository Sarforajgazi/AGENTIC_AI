from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()


# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------
def build_agent():
    return Agent(
        name="Quickstart Agent",
        model=Groq(id="qwen/qwen3.8-27b"),
        #model=OpenAIResponses(id="gpt-5.2"),
        tools= [
            DuckDuckGoTools(),YFinanceTools(all=True)
        ],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
        markdown= True,
        add_datetime_to_context= True,
        #debug_mode=True
    )



# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------

#openai_agent = build_agent()
groq_agent = build_agent()

groq_agent.print_response("Share the NVDA stock price and analyst recommendations")
