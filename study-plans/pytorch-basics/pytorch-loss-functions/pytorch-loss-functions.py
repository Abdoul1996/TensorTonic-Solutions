import torch

def compute_loss(pred: torch.Tensor, target: torch.Tensor, method: str, delta: float = 1.0) -> float:
    """
    Returns the mean loss as a Python float.
    """
    if method == "mse":
      error = pred - target
      loss =torch.mean(error**2)
      return loss.item()
    elif method == 'huber':
      error= pred - target
      a = torch.abs(error)
      condition = a <= delta
      loss = torch.where(condition, (0.5 * error**2), delta * (a - 0.5 *delta))
      loss_mean = torch.mean(loss)
      return loss_mean.item()
    elif method == 'cross_entropy':
      loss_fn = torch.nn.CrossEntropyLoss()
      return loss_fn(pred, target).item()
  
    
    
