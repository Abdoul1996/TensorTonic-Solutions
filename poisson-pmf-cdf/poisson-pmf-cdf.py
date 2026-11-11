import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    # step 1: computing the PDF 
    numerator = math.exp(- lam) * lam**k
    denominator = math.factorial(k)
    pmf = numerator / denominator

    # step 2 : computing the CDF 
    cdf = 0.0
    for i in range(k+1):
      prob = (math.exp(-lam) * lam**i) / math.factorial(i)
      cdf += prob

    return {
      "pmf":pmf,
      "cdf": cdf
    }
      