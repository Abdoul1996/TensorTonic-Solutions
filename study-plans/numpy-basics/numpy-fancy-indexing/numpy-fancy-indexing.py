import numpy as np

def select_by_index(arr: list, indices: list, axis: int) -> np.ndarray:
    """
    Returns a 2D float64 array of the selected rows or columns.
    """
    arr = np.array(arr, dtype=np.float64)
    return np.take(arr, indices, axis)
