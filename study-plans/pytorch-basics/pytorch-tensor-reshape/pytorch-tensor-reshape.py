import torch

def reshape_tensor(x: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """
    x = torch.tensor(x, dtype=torch.float32)

    if op == 'flatten':
      return x.flatten()
    elif op == 'squeeze':
      return x.squeeze()
    elif op == 'transpose':
      return x.T
    
