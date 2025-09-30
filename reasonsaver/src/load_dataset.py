from datasets import load_dataset
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "prompts.json"

def load_prompts(limit: int = 10000):
    # Load the ELI5 dataset (explain-like-I’m-5 questions)
    ds = load_dataset("eli5", split=f"train[:{limit}]")

    # Extract just the questions
    prompts = [q for q in ds["title"] if q and isinstance(q, str)]

    with open(DATA_PATH, "w") as f:
        json.dump(prompts, f, indent=2)

    print(f"Saved {len(prompts)} prompts → {DATA_PATH}")

if __name__ == "__main__":
    load_prompts(limit=10000)
