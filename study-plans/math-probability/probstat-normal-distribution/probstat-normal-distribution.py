from scipy.stats import norm
import numpy as np 
from math import pi, erf 

def cdf_at(point: float, mu: float, sigma: float) -> float:
    z = (point - mu) / sigma
    return (1/2) * (1 + erf((1/np.sqrt(2)) * z))

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """
    z_score = (x - mu) / sigma

    pdf = (1/(sigma * np.sqrt(2*pi))) * np.exp((-1/2) * (z_score**2))

    cdf = cdf_at(x, mu, sigma)

    a = mu - sigma
    b = mu + sigma
    prob_within_1_std = cdf_at(b, mu, sigma) - cdf_at(a, mu, sigma)

    return {
        "z_score": np.round(z_score, 4),
        "cdf": np.round(cdf,4),
        "pdf": np.round(pdf,4),
        "prob_within_1_std": np.round(prob_within_1_std,4)
    }