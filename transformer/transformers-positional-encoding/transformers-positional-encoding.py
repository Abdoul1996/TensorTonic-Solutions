import numpy as np
import math 

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Returns the sinusoidal position matrix.
    """
    arr = np.zeros((seq_length, d_model), dtype=np.float64)

    for pos in range(seq_length):
      for dim in range(d_model):
        
        # pair indexes a sine-cosine 
        i = dim // 2 
        angle_theta = pos / (10000**(2*i/d_model))

        if dim % 2 == 0: # even 
          arr[pos, dim] = math.sin(angle_theta)
        else: # odd 
          arr[pos,dim] =  math.cos(angle_theta)

    return arr