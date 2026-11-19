import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    """
    Returns the matrix-vector product as a float64 array.
    """
    A = np.asarray(A, dtype=float)
    x = np.asarray(x, dtype=float)

    return A @ x