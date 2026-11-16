import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    a_x_b = np.dot(a,b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    magnitude = norm_a * norm_b

    return float(np.where(norm_a == 0 or norm_b == 0, 0.0, a_x_b / magnitude))