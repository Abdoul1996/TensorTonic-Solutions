import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    # step 1: initilize 
    X = np.asarray(X, dtype=float)
    N = len(X)

    # step 2: compute the mean and correlation 
    mu = np.mean(X, axis=0)
    X_center = X - mu 
    covariance = np.dot(X_center.T, X_center) / (N- 1)

    # step 3: calculating standard deviation 
    std = np.std(X, axis=0, ddof=1)
    denominator = np.outer(std, std)

    with np.errstate(divide="ignore", invalid="ignore"):
      pearson_correlation = np.where(
        denominator== 0,
        np.nan, 
        covariance / denominator
    )
    return pearson_correlation
  
    
    