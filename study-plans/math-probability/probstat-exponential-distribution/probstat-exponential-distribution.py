from math import exp

def exponential_distribution(lam: float, t: float) -> dict:
    """
    Returns the PDF, CDF, survival probability, mean, and variance.
    """
    pdf = lam * exp(-(lam * t))
    cdf = 1 - exp(-(lam * t))
    survival = 1 - cdf
    mean = 1 / lam
    variance = 1 / (lam ** 2)

    return {
        "cdf": round(float(cdf), 4),
        "mean": round(float(mean), 4),
        "pdf": round(float(pdf), 4),
        "survival": round(float(survival), 4),
        "variance": round(float(variance), 4)
    }
