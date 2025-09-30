import json
from pathlib import Path
from scorer import score
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

#setting up tracer
trace.set_tracer_provider(TracerProvider()) #central object to set up observability enginet
tracer = trace.get_tracer(__name__) #provides tracer to use in this file/module
span_processor = SimpleSpanProcessor(ConsoleSpanExporter()) #processor decides what to do when a span ends. the simple one means to immediately export each span. consolespanexporter is where spans go like jaegar, file,etc
trace.get_tracer_provider().add_span_processor(span_processor)




def main(input_path="data/completions.json", output_path="data/evaluations.json"):
    input_path = Path(input_path)
    output_path = Path(output_path)

    with tracer.start_as_current_span("evaluation-run"):
        if not input_path.exists():
            raise FileNotFoundError(f"Missing {input_path}. Run main.py first.")
            
        with open(input_path) as f:
            completions = json.load(f)

        evaluations = []
        for item in completions:
            prompt = item["prompt"]
            completion = item["completion"]

            #trace each scoring step
            with tracer.start_as_current_span("scoring"):
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
