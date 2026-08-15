import math 
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    result = []
    for i in range(len(values)):
        result.append(math.log(1+values[i]))
    return result