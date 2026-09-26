import numpy as np
from math import sqrt
def standard_errors(samples: list) -> dict:
    """
    Returns each sample standard error and their mean.
    """
    SE = []

    for sample in samples:
      sample = np.asarray(sample, dtype='float64')
      n = len(sample)
      standard_deviation = np.std(sample, ddof=1)
      standard_errors = standard_deviation / sqrt(n)
      SE.append(round(float(standard_errors), 4))

    mean_se = np.mean(SE)

    return {
      "mean_se": round(mean_se,4),
      "standard_errors": SE
    }

    
