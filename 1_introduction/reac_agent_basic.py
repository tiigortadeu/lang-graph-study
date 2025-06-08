from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
from langchain_community.tools import TavilySearchResults
from datetime import datetime


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

search_tool = TavilySearchResults(search_depth="basic")

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """returns the current date and time in the given format"""

    current_time = datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke({"input": "qual o próximo jogo da fura na kings leagueverifiqu"})


#esult = agent.invoke({"input": "Give me a tweet about são paulo weather?"})

#print(result)

