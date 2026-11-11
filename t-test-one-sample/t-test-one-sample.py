import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here

    # step 1: compute the mean of sample 
    mu = np.mean(x)
    n = len(x)
  
    # step 2 : compute sample standard deviation 
    s = np.sqrt(1/(n-1) * np.sum((x-mu)**2))

    # step 3: Handle edge cases and then compute t-test 
    if s == 0:
      if mu == mu0:
        return 0.0 
      elif mu < mu0:
        return float('-inf')
      else:
        return float('inf')

    else:
      return float((mu - mu0) / (s / np.sqrt(n)))

  