import numpy as np

def discrete_moments(values: list, probabilities: list) -> list:
    """
    Returns the first moment, second moment, variance, and standard deviation.
    """
    values = np.asarray(values, dtype='float64')
    probabilities = np.asarray(probabilities, dtype='float64')
    
    first_moment = float(np.sum(values * probabilities))
    second_moment = float(np.sum(values ** 2 * probabilities))
    variance =float(max(0.0, second_moment - ((first_moment)**2)))
    std = float(np.sqrt(variance))

    return [ round(value, 4) for value in [first_moment, second_moment, variance, std]]
