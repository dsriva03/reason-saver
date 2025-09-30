#create an entrypoint for reason-saver
import argparse
from evaluate import main as evaluate_main

def run():
    parser = argparse.ArgumentParser(
        description="ReasonSaver CLI: evaluate completions at scale"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/completions.json",
        help="Path to completions.json file"

    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/evaluations.json",
        help="Where to save evaluations"
    )

    args = parser.parse_args()

    #call evaluate.py main function
    evaluate_main(input_path=args.input, output_path=args.output)

if __name__ == "__main__":
    run()


