import numpy as np

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """
    v = np.array(v, dtype=float)

    l1_norm = np.linalg.norm(v, ord=1)
    l2_norm = np.linalg.norm(v, ord=2)
    max_norm = np.linalg.norm(v, ord=np.inf)
    return np.asarray([float(l1_norm), float(l2_norm), float(max_norm)])