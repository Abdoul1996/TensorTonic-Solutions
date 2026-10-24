import torch

def batch_norm(X: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as X.
    """
    X = X.to(dtype=torch.float32)

    N = len(X)

    # step 1: batch mean 
    batch_mean = 1/N * torch.sum(X, dim=0, keepdim=True)

    # step 2: batch variance square 
    batch_variance = 1/N * ((X - batch_mean)**2).sum(dim=0, keepdim=True)

    # step 3: Normalize 
    Y = gamma * ((X - batch_mean) / torch.sqrt(batch_variance + eps)) + beta

    return Y 

    
