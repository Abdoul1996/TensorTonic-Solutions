import numpy as np
from scipy.stats import norm
from math import sqrt

def clt_confidence_interval(data: list, confidence: float) -> list:
    """
    Returns the sample mean, standard error, and confidence-interval endpoints.
    """
    n = len(data)
    mean = np.mean(data, dtype="float64")
    std = np.std(data, dtype="float64", ddof=1)
    SE = std / sqrt(n)

    alpha = 1 - confidence
    z_critical = norm.ppf(1-alpha / 2)

    ME = z_critical * SE

    lower_bound = mean - ME
    upper_bound = mean + ME 
    
    return [round(mean,4), round(SE, 4), round(lower_bound, 4), round(upper_bound, 4)]

    
  

    
    
    
    
