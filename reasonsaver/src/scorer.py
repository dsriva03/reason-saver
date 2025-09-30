# reasonsaver/src/scorer.py
from sentence_transformers import SentenceTransformer
from torch.nn.functional import cosine_similarity
import torch

# Load once (fast small model)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def score(response_text: str):
    """
    Returns a similarity score of the response to a generic 'reasoning quality' anchor.
    Minimal but real: compares completion to a neutral anchor prompt.
    """
    # anchor can be any stable text—acts like a reference heuristic
    anchor = "Provide a clear, step-by-step, logically correct explanation with no hallucinations."

    embs = _model.encode([anchor, response_text], convert_to_tensor=True)
    anchor_emb, resp_emb = embs[0].unsqueeze(0), embs[1].unsqueeze(0)
    sim = cosine_similarity(anchor_emb, resp_emb).item()

    # map cosine [-1,1] to [0,1]
    norm = (sim + 1) / 2
    return {
        "score": round(norm, 4),
        "reason": f"Cosine(sim) vs. anchor = {sim:.4f} → normalized {norm:.4f}"
    }
