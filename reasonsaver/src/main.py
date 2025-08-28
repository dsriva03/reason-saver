from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import time

#loading api key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load prompts
with open("data/prompts.json") as f:
    prompts = json.load(f)

# Loop through prompts
completions = []
for prompt in prompts:
    print("Running prompt:", prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    completions.append({
        "prompt": prompt,
        "completion": answer
    })

    time.sleep(1)

# Save completions
with open("data/completions.json", "w") as f:
    json.dump(completions, f, indent=2)
