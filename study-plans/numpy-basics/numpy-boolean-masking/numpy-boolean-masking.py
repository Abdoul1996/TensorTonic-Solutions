import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    arr = np.array(data, dtype=np.float64)

    # first layer 
    mask = np.where(arr > threshold, 1.0, 0.0)
    

  # second layer 
    mask2 = np.any(arr > threshold, axis=1)
    mask2 = mask2[:, np.newaxis]
    arr2 = np.where(mask2,arr, 0.0)
  
    # layer 3 
    mask3 = np.all(arr>threshold, axis=1)
    mask3 = mask3[:, np.newaxis]
    arr3 = np.where(mask3, arr, 0.0)
  
    return np.stack([mask, arr2, arr3])

  
