from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI


generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         "You are a twitter techie influencer assistent tasked with writing excellent twitter posts."
         "Generate the best twitter post possible for user's request."
         "If the user provides critique, respond with a revised version of your previous answer."
         
         ),
        MessagesPlaceholder(variable_name="messages"), #Aqui servirá para colocar o histórico todo de mensagens sempre
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet."
            "Generate critique and recommendations for the tweet."
            "Always provide detailed recommendations, incluiding requests for length, virality, style, etc."

        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

generation_chain = generation_prompt | llm 
reflection_chain = reflection_prompt | llm 






 


