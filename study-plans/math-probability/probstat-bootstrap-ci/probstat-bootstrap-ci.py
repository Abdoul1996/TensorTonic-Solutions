import numpy as np

def bootstrap_ci(data: list, n_bootstraps: int, confidence: float, seed: int) -> list:
    """
    Returns the bootstrap mean and percentile confidence interval.
    """
    # n and original mean
    n = len(data)
    mu = np.mean(data)
    means = []

    rng = np.random.RandomState(seed)

    for i in range(n_bootstraps):
      resampling = rng.choice(data, n, replace=True)
      
      means.append(np.mean(resampling))
      
    alpha = 1 - confidence
  
    lower_percentile = 100 * (alpha / 2)
    upper_percentile = 100 * (1-(alpha / 2))

    lower = np.percentile(means, lower_percentile)
    upper = np.percentile(means, upper_percentile)
    boot_means = np.mean(means)

    return [ boot_means, lower, upper]
  
    

    
