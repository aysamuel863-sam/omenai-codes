import sys
import os
import openai  
from openai import OpenAI
print(f"Python: {sys.executable}")
print(f"OpenAI Package: {openai.__version__}")
print(f"API key exists: {bool(os.getenv("NVIDIA_API_KEY2"))}")
key = os.getenv("NVIDIA_API_KEY")
print(f"Key exists: {key is not None}")
print(f"Key length: {len(key) if key else 0}")
print(f"Starts with nvapi: {key.startswith("nvapi-") if key else False}")
print(key[:7])
print(key[-4:])
client = OpenAI(
    base_url = "https://integrate.api.nvidia.com/v1",
    api_key = os.getenv("NVIDIA_API_KEY2")
)

messages = [{
    "role": "system",
    "content": "You are a helpful AI Tutor. Explain technical topics clearly at an SS2 student"
}]

while True:
    question = input("You: ")
    
    if question.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model = "nvidia/nemotron-3-super-120b-a12b",
        messages = messages,
        max_tokens = 700
    )

    answer = response.choices[0].message.content
    
    messages.append({
        "role": "assistant",
        "content": answer
    })
    print(f"AI: {answer}")