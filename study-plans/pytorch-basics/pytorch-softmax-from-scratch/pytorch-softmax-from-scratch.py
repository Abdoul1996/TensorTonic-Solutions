import torch

def softmax(logits: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 probability tensor with the same shape as logits.
    """
    z = logits.to(dtype=torch.float32)

    z_stable = z - torch.max(z, dim=1, keepdim=True).values

    numerator = torch.exp(z_stable)
    denominator = torch.sum(numerator, dim=1, keepdim=True)
    prob = numerator / denominator 

    return prob
    
