# 1. Solution

# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash",
#     temperature = 0.7
# )

# response = llm.invoke("What is the Capital of India?")

# print(response.content)


# 2. Solution

# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash",
#     temperature = 0.7
# )

# response = llm.invoke("What is the Capital of India?")

# print(response.response_metadata)


# 3. Solution
# from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0
# )

# response = model.invoke(
#     "Write a short sentence about AI."
# )

# print("Usage Metadata:")
# print(response.usage_metadata)

# print("\nInput Tokens:")
# print(response.usage_metadata.get("input_tokens"))

# print("\nOutput Tokens:")
# print(response.usage_metadata.get("output_tokens"))

# print("\nTotal Tokens:")
# print(response.usage_metadata.get("total_tokens"))


# 5. Solution

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

model_with_tools = model.bind_tools([add])

response = model_with_tools.invoke(
    "What is 10 + 20? Use the add tool."
)

print("CONTENT:")
print(response.content)

print("\nTOOL CALLS:")
print(response.tool_calls)

print("\nINVALID TOOL CALLS:")
print(response.invalid_tool_calls)


if response.tool_calls:
    print("\nValid tool call generated!")

    for tool_call in response.tool_calls:
        print("Tool Name:", tool_call["name"])
        print("Arguments:", tool_call["args"])

else:
    print("\nNo valid tool call generated.")


if response.invalid_tool_calls:
    print("\nInvalid tool calls found:")
    print(response.invalid_tool_calls)

else:
    print("\nNo invalid tool calls found.")