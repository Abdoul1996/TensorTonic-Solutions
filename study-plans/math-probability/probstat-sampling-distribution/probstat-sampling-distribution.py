from math import sqrt
from scipy.stats import norm

def sampling_distribution(mu: float, sigma: float, n: int, threshold: float) -> dict:

    sampling_mean = mu
    sampling_std = sigma / sqrt(n)

    z_score = (threshold - mu) / sampling_std

    return {
        "prob_below_threshold": round(float(norm.cdf(z_score)), 4),
        "sampling_mean": round(float(sampling_mean), 4),
        "sampling_std": round(float(sampling_std), 4)
    }