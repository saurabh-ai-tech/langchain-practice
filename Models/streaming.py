# 1. Solution
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 0.7
)

prompt = "Explain AI in 3 short sentences."

for chunk in llm.stream(prompt):
    if chunk.content:
        # flush=True forces the buffer to output immediately to stdout
        print(chunk.content, end="", flush=True)

print()
