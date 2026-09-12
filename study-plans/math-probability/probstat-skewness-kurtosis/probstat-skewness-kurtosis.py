import numpy as np

def skewness_kurtosis(data):
    """
    Returns: dict with 'skewness', 'kurtosis', and interpretation strings.
    """

    data = np.array(data, dtype=float)

    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)

    # Part I : skewness 
    # standard deviation 
    z = (data - mean) / std 

    # sum of cubed standard deviation 
    sum_cubed = np.sum(z**3)

    # correction
    correction =  n / ((n-1) * (n-2))
    g1 = correction * sum_cubed 

    if g1 > 0.5:
        skew_interpretation = "right-skewed"
    elif g1 < - 0.5:
        skew_interpretation = "left-skewed"
    else:
        skew_interpretation = "approximately symmetric"


    # Part 2 : kurtosis

    correction_g2 = (n * (n+1)) / ((n-1) * (n-2) * (n-3))
    
    sum_fourth = np.sum(z**4)
    
    second_correction = (3 * (n-1)**2) / ((n-2) * (n-3))
    
    g2 = correction_g2 * sum_fourth - second_correction

    if g2 > 1:
        kurtosis_interpretation = "leptokurtic"
    elif g2 < -1:
        kurtosis_interpretation = "platykurtic"
    else:
        kurtosis_interpretation = "mesokurtic"


    return {
        "skewness": np.round(g1,4),
        "kurtosis": np.round(g2, 4),
        "skew_interpretation": skew_interpretation,
        "kurtosis_interpretation": kurtosis_interpretation
    }



    
        
    

    
    
    





