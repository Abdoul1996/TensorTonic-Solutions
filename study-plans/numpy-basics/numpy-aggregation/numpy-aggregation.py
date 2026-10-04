import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    arr = np.array(data, dtype=np.float64)
    mean = np.mean(arr, axis)
    std = np.std(arr, axis)
    minimum = np.min(arr, axis)
    maximum = np.max(arr, axis)

    return np.stack([mean, std, minimum, maximum])
