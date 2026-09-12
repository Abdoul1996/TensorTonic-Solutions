import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    var = np.var(x, ddof=1)
    std = np.std(x, ddof=1)

    return {
        "variance": var,
        "std_dev": std
    }