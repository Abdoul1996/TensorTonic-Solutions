import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    arr = np.array(data, dtype=np.float64)

    # first layer:
    mask1 = np.where(arr > threshold, 1.0,0.0)
    arr1 = mask1

    # second layer:
    mask2 = np.any(arr > threshold, axis=1)
    arr2 = np.where(mask2[:, None], arr, 0.0)

    # third layer:
    mask3 = np.all(arr > threshold, axis=1)
    arr3 = np.where(mask3[:, None], arr, 0.0)

    arr_final = np.stack([arr1, arr2, arr3])

    return arr_final 
    
