# 1. Solution
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# Load a local image
image = Image.open("architecture.jpeg")

# Interleave text and image blocks in the contents list
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        "Analyze the data shown in this chart and highlight key trends:",
        image,
    ],
)

print(response.text)