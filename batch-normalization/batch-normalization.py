import numpy as np

def batch_norm_forward(x: list, gamma: list, beta: list, eps: float = 1e-5) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    beta = np.asarray(beta, dtype=float)

    if x.ndim == 2:
        # step 1: Computing the mean and variance  
        mu = np.mean(x, axis=0, keepdims=True)
        var = np.var(x, axis=0, keepdims=True)
    
        # step 2: Scalling stats 
        scaled = (x - mu) / (np.sqrt(var + eps))
    
        # step 3: Normalized 
        normalized = gamma * scaled + beta
    
        return normalized
    elif x.ndim == 4:

        # Step 1: Reshape gamma and betta
        gamma = gamma.reshape(1,x.shape[1],1,1)
        beta = beta.reshape(1, x.shape[1], 1,1)

        # step 2: compute the mean and var 
        mu = np.mean(x, axis=(0,2,3), keepdims=True)
        var = np.var(x, axis=(0,2,3), keepdims=True)

        # step 3: Scaled the stats 
        scaled = (x-mu) / (np.sqrt(var + eps))

        # step 4: Normalized the scaled 
        normalized = gamma * scaled + beta

        return normalized
        
        