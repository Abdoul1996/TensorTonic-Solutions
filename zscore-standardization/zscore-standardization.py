import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.asarray(X, dtype=np.float64)
    
    mu = np.mean(X, axis=axis, keepdims=True)
    
    sigma = np.std(X, axis=axis, keepdims=True)
    
    safe_sigma = np.where(sigma> eps, sigma, 1.0)

    z_score = (X - mu) / safe_sigma

    return z_score