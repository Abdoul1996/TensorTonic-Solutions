import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    angles = np.array(angles, dtype=np.float64)

    sin_value = np.sin(angles)
    cos_value = np.cos(angles)
    tan_value = np.tan(angles)

    return np.stack([sin_value, cos_value, tan_value])
