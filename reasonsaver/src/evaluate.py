# reasonsaver/src/evaluate.py
import json
from pathlib import Path

# If evaluate.py is in the same folder as scorer.py, this import works:
from scorer import score

COMPLETIONS_PATH = Path(__file__).resolve().parents[1] / "data" / "completions.json"
EVALUATIONS_PATH = Path(__file__).resolve().parents[1] / "data" / "evaluations.json"

def main():
    if not COMPLETIONS_PATH.exists():
        raise FileNotFoundError(f"Missing {COMPLETIONS_PATH}. Run main.py first.")

    with open(COMPLETIONS_PATH) as f:
        completions = json.load(f)

    evaluations = []
    for item in completions:
        prompt = item["prompt"]
        completion = item["completion"]
        result = score(completion)  #current fake score function
        evaluations.append({
            "prompt": prompt,
            "completion": completion,
            "score": result["score"],
            "reason": result["reason"]
        })

    with open(EVALUATIONS_PATH, "w") as f:
        json.dump(evaluations, f, indent=2)

    print(f"Wrote {len(evaluations)} evaluations → {EVALUATIONS_PATH}")

if __name__ == "__main__":
    main()
