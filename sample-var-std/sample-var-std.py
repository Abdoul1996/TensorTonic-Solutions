import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    variance = np.var(x, ddof=1)
    std = np.std(x, ddof=1)

    return {
      "variance": float(variance),
      "standard_deviation": float(std)
    }