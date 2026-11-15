import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y = np.asarray(y)
    K = num_classes

    # step 1: Determine K 
    if K is None:
      K = max(y) + 1
    return np.eye(K)[y]