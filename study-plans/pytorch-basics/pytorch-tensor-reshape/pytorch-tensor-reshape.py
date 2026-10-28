import torch

def reshape_tensor(x: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """

    x = x.to(dtype=torch.float32)

    if op == 'view':
      return torch.view(x)
    elif op == 'flatten':
      return torch.flatten(x)
    elif op == 'squeeze':
      return x.squeeze()
    elif op == 'unsqueeze':
      return x.unsqueeze(dim=0)
    elif op == 'transpose':
      return x.T
    
