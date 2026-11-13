from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    mean = np.mean(x)
    median = np.median(x)
    freq = Counter(x)

    mode = max(freq, key=freq.get)

    return {
      "mean": float(mean),
      "median": float(median),
      "mode": float(mode)
    }

    