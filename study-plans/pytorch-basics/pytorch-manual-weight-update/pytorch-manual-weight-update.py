import torch
import torch.nn as nn

def manual_train_step(model: nn.Module, X: torch.Tensor, y: torch.Tensor, criterion: nn.Module, lr: float) -> float:
    """
    Returns the pre-update batch loss as a Python float.
    """
    model.zero_grad()
    # step 1: Forward pass 
    pred = model(X)

    # step 2: Loss 
    loss = criterion(pred, y)

    # step 3: Backward pass 
    loss.backward()

    # step 4: Updating parameters manually
    with torch.no_grad():
      for param in model.parameters():
        if param.requires_grad:
          param -= lr * param.grad

          # step 5: clear gradient 
          param.grad.zero_()

    return loss.item()
  
    
