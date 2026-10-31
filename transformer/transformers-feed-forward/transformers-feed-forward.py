import numpy as np

def relu(x: np.ndarray):
  relu = np.where(x > 0, x, 0)
  return relu

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Returns the position-wise feed-forward output.
    """
    z1 = np.dot(x,W1) + b1
    hidden = relu(z1)
    output = hidden @ W2 + b2
    return output
    