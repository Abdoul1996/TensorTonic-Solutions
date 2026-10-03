import numpy as np

def norm_diff(a: list, b: list, lo: float, hi: float) -> np.ndarray:
    """
    Returns a float64 array of absolute normalized differences.
    """
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)

    a_clip = np.clip(a, lo, hi)
    b_clip = np.clip(b, lo, hi)

    numeralized_diff = np.abs(a_clip - b_clip) / (hi - lo)
    return numeralized_diff
