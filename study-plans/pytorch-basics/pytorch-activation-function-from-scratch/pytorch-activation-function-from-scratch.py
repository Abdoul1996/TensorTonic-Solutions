import torch
import torch.nn as nn 

def activate(x: torch.Tensor, method: str = "relu") -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as x.
    """
    x = torch.tensor(x, dtype=torch.float32)
  
    if method == 'relu':
      ReLu = torch.nn.ReLU()
      return ReLu(x)
    elif method == 'leaky_relu':
      LeakyReLU = torch.nn.LeakyReLU(negative_slope=0.01)
      return LeakyReLU(x)
    elif method == 'sigmoid':
      sigmoid = torch.nn.Sigmoid()
      return sigmoid(x)
    elif method == 'tanh':
      tanh = torch.nn.Tanh()
      return tanh(x)
      
    
    
