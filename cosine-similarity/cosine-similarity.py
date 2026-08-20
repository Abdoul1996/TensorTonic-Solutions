import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here

    a = np.asarray(a, float)
    b = np.asarray(b, float)
    
    cosine = 0 
   
    dot_product = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b ==0:
        return 0.0

    cosine += dot_product / (norm_a * norm_b)

    return cosine