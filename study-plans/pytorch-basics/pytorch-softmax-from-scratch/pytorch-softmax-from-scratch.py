import torch

def softmax(logits: torch.Tensor) -> torch.Tensor:
    """
    Returns a float32 probability tensor with the same shape as logits.
    """
    z = torch.tensor(logits, dtype=torch.float32)

    z_stable = z - z.max(dim=1, keepdim=True).values

    exp_z = torch.exp(z_stable)
  
    denominator = (exp_z).sum(dim=1, keepdim=True)

    prob = exp_z / denominator

    return prob

    