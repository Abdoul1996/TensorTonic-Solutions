import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    numerator = np.exp(x) - np.exp(-x)
    denominator = np.exp(x) + np.exp(-x)

    return numerator / denominator 