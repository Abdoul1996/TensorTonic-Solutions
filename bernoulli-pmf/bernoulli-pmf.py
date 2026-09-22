import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x = np.asarray(x, dtype=int)
    p = np.asarray(p, dtype=np.float64)

    pmf = (p**x) * (1-p)**(1-x)
    mean = float(p)
    variance = float(p - (p**2))

    return {
        "pmf": pmf,
        "mean": mean,
        "variance": variance 
    }