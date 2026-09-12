import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.array(x, dtype='float64')

    n = len(x)
    mean = np.mean(x)

    correction = 1 / (n-1)
    sum_center = np.sum((x-mean)**2)

    variance = float(correction * sum_center)

    std = float(np.sqrt(variance))

    return {
        "variance": variance,
        "standard_deviation": std
    }