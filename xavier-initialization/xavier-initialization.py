import math
import numpy as np 

def xavier_initialization(W: list, fan_in: int, fan_out: int) -> list:
    """
    Returns the weights mapped to the Xavier uniform range.
    """
    # Write code here
    W = np.asarray(W, dtype=float)
    xavier_uniform = math.sqrt(6/(fan_in + fan_out))
    W = W * 2 * xavier_uniform - xavier_uniform

    return W 