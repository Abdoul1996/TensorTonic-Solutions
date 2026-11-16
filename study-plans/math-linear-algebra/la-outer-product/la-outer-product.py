import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)

    return np.outer(u,v)