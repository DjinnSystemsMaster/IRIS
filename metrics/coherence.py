"""Computes cosine similarity Λ(S) between successive agent states."""
import numpy as np

def compute_coherence(state_history):
    if len(state_history) < 2:
        return 1.0
    v1 = np.array(state_history[-2])
    v2 = np.array(state_history[-1])
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)
