from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Country(BaseModel):
    """Information about a country"""

    name: str = Field(description="The name of the country")
    language: str = Field(description="The language of the country")
    capital: str = Field(description="The capital of the country")

structured_llm = llm.with_structured_output(Country)
structured_llm

# Descomente a linha abaixo para testar
# result = structured_llm.invoke("Tell me about Brasil?")
# print(result) 