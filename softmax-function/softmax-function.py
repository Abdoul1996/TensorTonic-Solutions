import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here

    x = np.asarray(x, dtype=float)

    if x.ndim == 2: 
      # step 1: compute numerator 
      m = np.max(x, axis=1, keepdims=True)
      numerator = np.exp(x - m)
  
      # step 2: compute denominator 
      denominator = np.sum(numerator, axis=1, keepdims=True)
  
      return numerator / denominator 
    elif x.ndim == 1:
       # step 1: compute numerator 
      m = np.max(x)
      numerator = np.exp(x - m)
  
      # step 2: compute denominator 
      denominator = np.sum(numerator)
  
      return numerator / denominator 
      