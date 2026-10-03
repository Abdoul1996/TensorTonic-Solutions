import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    data = np.array(data, dtype=np.float64)

    col_mean = np.mean(data, axis=0)
    col_std = np.std(data, axis=0)
    standardized = (data - col_mean) / col_std
    return standardized
