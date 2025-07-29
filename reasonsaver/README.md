# 🧠 ReasonSaver

**ReasonSaver** is a lightweight, extensible tool for evaluating the *reasoning quality* of GPT-generated outputs.

It takes in prompts and model completions, and scores them based on how coherent, logical, and well-justified the responses are — using either GPT-based self-critique or custom scoring logic. Built for LLM debugging, prompt optimization, and interpretability research.

> Think of it as a microscope for GPT reasoning.

---

## ✨ Features

- 🔁 Generate multiple completions per prompt using OpenAI’s API  
- 📊 Score each response on reasoning quality (0–1 scale)  
- 🧠 Self-critique scoring via GPT or custom rule-based logic  
- 📁 Outputs clean JSON logs of prompts, completions, and evaluations  
- ⚙️ Easily extensible with manual or OCaml-based scoring (coming soon)  
- 🧪 Useful for prompt engineering, model comparison, and hallucination detection

---

## 📂 Project Structure

```
reasonsaver/
├── main.py              # Run end-to-end flow: generate & evaluate
├── prompts.json         # Input prompts
├── completions.json     # Raw GPT responses
├── evaluations.json     # Scored outputs
├── scorer.py            # Scoring logic (GPT-based or rule-based)
├── ocaml_scorer.ml      # (Optional) Type-safe scoring module
├── README.md
```

---

## 🚀 Example Use

```bash
python main.py
```

Generates completions from GPT, scores them, and saves results to `completions.json` and `evaluations.json`.

---

## 📈 Sample Output

```json
{
  "prompt": "Why do people say the Earth is round?",
  "response": "People believe the Earth is round due to satellite imagery and centuries of scientific consensus.",
  "score": 0.94,
  "reason": "Clear, fact-based explanation with no logical fallacies."
}
```

---

## 💡 Future Ideas

- ✅ OCaml-based type-safe scoring module  
- ✅ Leaderboard visualization  
- ✅ Rule-based hallucination detection  
- ✅ Human-in-the-loop review UI  
- ✅ Comparison across GPT-4 vs GPT-3.5

---

## 🧙‍♀️ Built With

- Python 3.10+  
- `openai`  
- (Optionally) OCaml + `yojson` + `dune`

---

## 🐛 Made by two worms and a dream.
