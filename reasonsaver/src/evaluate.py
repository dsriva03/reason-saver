import json
from pathlib import Path
from scorer import score

def main(input_path="data/completions.json", output_path="data/evaluations.json"):
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Missing {input_path}. Run main.py first.")

    with open(input_path) as f:
        completions = json.load(f)

    evaluations = []
    for item in completions:
        prompt = item["prompt"]
        completion = item["completion"]
        result = score(completion)
        evaluations.append({
            "prompt": prompt,
            "completion": completion,
            "score": result["score"],
            "reason": result["reason"]
        })

    with open(output_path, "w") as f:
        json.dump(evaluations, f, indent=2)

    print(f"Wrote {len(evaluations)} evaluations → {output_path}")
