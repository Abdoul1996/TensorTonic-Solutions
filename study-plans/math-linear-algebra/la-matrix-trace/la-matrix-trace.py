import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """
    A = np.asarray(A, dtype=float)

    mask = np.eye(A.shape[0])
    mask_A = A * mask

    return float(np.sum(mask_A))