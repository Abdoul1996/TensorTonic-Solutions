import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    x = np.asarray(x, dtype=float)
    percenti = np.percentile(x, q)

    return percenti
    
