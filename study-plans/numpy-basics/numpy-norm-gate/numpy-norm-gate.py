import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    X = np.array(X, dtype=np.float64)
    W = np.array(W, dtype=np.float64)

    # step 1
    Z = np.dot(X, W)

    # step: 2 compute norm L2 
    norm = np.sqrt(np.sum(Z**2, axis=1))

    # step 3: compute the gate 
    gate = norm  >= threshold
    gate = gate[:, np.newaxis]

    # step 4: compute Y = gate * Y 
    Y = gate * Z 
    return Y 

  
    
