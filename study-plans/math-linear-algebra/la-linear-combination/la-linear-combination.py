import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    v = np.asarray(vectors, dtype=float)
    c = np.asarray(coefficients, dtype=float)

    return c @ v 