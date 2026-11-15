import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    X = np.asarray(X, dtype=float)

    # Step 1: Identify missing values
    mask = np.isnan(X)

    # Step 2: Calculate column statistics
    if strategy == "mean":
        values = np.nanmean(X, axis=0)
    elif strategy == "median":
        values = np.nanmedian(X, axis=0)

    # Step 3: Handle columns containing only NaN
    values = np.where(np.isnan(values), 0.0, values)

    # Step 4: Replace missing values
    return np.where(mask, values, X)