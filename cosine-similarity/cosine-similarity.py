import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    dot_prod = np.dot(a,b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    result = np.where(
      norm_a == 0 or norm_b == 0,
      0.0,
      dot_prod / (norm_a * norm_b)
    )
    return float(result)