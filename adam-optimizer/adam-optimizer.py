import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    
    param = np.asarray(param, dtype=float)
    grad = np.asarray(grad, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)

    # step 1: Update the first moment
    first_mom = beta1 * m + (1-beta1) * grad

    # step 2: Update the second moment 
    second_mom = beta2 * v + (1-beta2) * grad**2

    # step 3: Bias Correction
    first_bias_correction = first_mom / (1 - beta1**t)
    second_bias_correction = second_mom / (1-beta2**t)

    # step 4: Parameter update
    param = param - (lr * first_bias_correction) / (np.sqrt(second_bias_correction) + eps)

    return (param, first_mom, second_mom)