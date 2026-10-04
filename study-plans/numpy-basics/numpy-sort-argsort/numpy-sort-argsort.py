import numpy as np

def sort_with_indices(data: list, axis: int) -> np.ndarray:
    """
    Returns a (2, m, n) float64 array of sorted values and source indices.
    """
    arr = np.array(data, dtype=np.float64)

    arr_sort = np.sort(arr, axis)

    idx_sort = np.argsort(arr, axis)
    return np.stack([arr_sort, idx_sort])
