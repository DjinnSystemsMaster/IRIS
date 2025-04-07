"""Calculates entropy H as state variance over a rolling window."""
import numpy as np

def compute_entropy(signal):
    return np.var(signal)
