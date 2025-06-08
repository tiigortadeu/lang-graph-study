from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, tool
from langchain_community.tools import TavilySearchResults
from datetime import datetime

# Carrega variáveis de ambiente (API keys)
load_dotenv()

# Inicializa o modelo Gemini Flash
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Configura a ferramenta de busca em tempo real
tavily_search = TavilySearchResults()
search_tool = Tool(
    name="Realtime Search",
    func=tavily_search,
    description="Useful for real-time searches (current events, sports matches, live data)"
)

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """returns the current date and time in the given format"""
    current_time = datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time



# Cria o agente com capacidade de busca
tools = [search_tool,get_system_time]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Exemplo de uso: próximo jogo do Corinthians
response = agent.invoke({"input": "What is the next match of Corinthians?"})
print(response["output"])
