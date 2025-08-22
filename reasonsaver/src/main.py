from dotenv import load_dotenv
import os
import openai
import json

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load prompts from file
with open("data/prompts.json") as f:
    prompts = json.load(f)

# Loop through prompts
for prompt in prompts:
    print("Running prompt:", prompt)
    # (you can now add your GPT call + scoring here)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["choices"][0]["message"]["content"]
    print("Answer:", answer)