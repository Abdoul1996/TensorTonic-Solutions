import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    # Step 1: Create the mask 
    mask = np.isnan(X)
    # step 2: Get the mean and median of X and replace the missing values  
    if strategy == "mean":
      mean = np.nanmean(X, axis=0)
      value = np.where(np.isnan(mean), 0.0, mean)
      return np.where(mask, value, X)
    elif strategy == "median":
      median = np.nanmedian(X, axis=0)
      value = np.where(np.isnan(median), 0.0, median)
      return np.where(mask, value, X)
    