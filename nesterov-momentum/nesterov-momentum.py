import numpy as np

def nesterov_momentum_step(w: list, v: list, grad: list, lr: float = 0.01, momentum: float = 0.9) -> dict:
    """
    Returns a dictionary with new_w and new_v.
    """
    # Write code here
    w = np.asarray(w, dtype=float)
    v = np.asarray(v, dtype=float)
    grad = np.asarray(grad, dtype=float)

    # step 1: compute the new velocity 
    v = momentum * v + lr * grad

    # step 2: compute the new weight 
    w = w - v 

    return {
      "new_w": w,
      "new_v": v
    }