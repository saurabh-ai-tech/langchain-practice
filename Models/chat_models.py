# 1. Solution 
# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash", 
#     temperature = 0.7
# )

# message = llm.invoke("Hi gemini How are you doing?")

# print(message.content)


# 2. Solution
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash", 
    temperature = 0.7
)

response_1 = llm.invok("What is Python?")
response_1 = llm.invok("Explain FastAPI in simple workds.")
response_1 = llm.invok("What is an AI Agent?")