import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    N = len(X)
    u = np.mean(X, axis=0)
    X_c = X - u 
    sampl_cov = np.dot(X_c.T, X_c)/ (N-1)
    return sampl_cov