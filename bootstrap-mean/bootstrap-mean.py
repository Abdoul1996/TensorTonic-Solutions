import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    # Step 1: draw every boostrap sample with replacement 
    x = np.asarray(x, dtype=float)
    N = len(x)
    rng = np.random.default_rng(seed)
    sample_mean = []
    for i in range(n_bootstrap):
        sample = rng.choice(x, size=N, replace=True)
        x_mean = np.mean(sample)
        sample_mean.append(x_mean)

    alpha = (1-ci) / 2
    
    lower = np.quantile(sample_mean, alpha)
    upper = np.quantile(sample_mean, 1-alpha)
    bootstrap_mean = np.mean(sample_mean)
    
    return {
        "bootstrap_mean": float(bootstrap_mean),
        "lower": float(lower),
        "upper":float(upper)
    }
        
    