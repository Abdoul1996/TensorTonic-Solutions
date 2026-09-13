from math import factorial, exp

def poisson_distribution(lam, max_k):
    """
    Returns: [pmf_list, cdf_at_max_k, p_zero] as a list.
    """
    pmf = []
    for k in range(max_k + 1):
        probability = float(round((lam**k * exp(-lam)) / factorial(k), 4))
        pmf.append(probability)

    cdf= round(sum(pmf),4)

    p_x_equal_0 = pmf[0]

    return [pmf, cdf, p_x_equal_0]
    