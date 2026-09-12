import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.array(x)

    mean =  np.mean(x)
    median = np.median(x)

    count = Counter(x)

    mode = count.most_common(1)[0][0]

    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }
    
    