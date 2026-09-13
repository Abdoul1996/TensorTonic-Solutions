from math import comb

def binomial_distribution(n, p, threshold):
    """
    Returns: dict with 'pmf' (list), 'mean', 'variance', 'tail_prob' as floats.
    """

    mean = round(n * p, 4)
    variance = round(n*p * (1-p), 4)

    pmf = []

    for k in range(n+1):
        probability = round(comb(n,k) * p**k * (1-p)**(n-k), 4)
        pmf.append(probability)
        
    prob_at_least = round(sum(pmf[threshold:]), 4) # at least treshold

    return {
        "pmf": pmf,
        "mean": mean,
        "variance": variance,
        "prob_at_least": prob_at_least
    }
    

    