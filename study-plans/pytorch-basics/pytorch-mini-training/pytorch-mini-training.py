import torch
import torch.nn as nn

def train_epoch(model: nn.Module, dataloader: torch.utils.data.DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer) -> float:
    """
    Returns the mean batch loss as a Python float.
    """
    model.train()

    total_loss = 0.0 
    numb_batch = 0.0 

    for X_batch, y_batch in dataloader:

      # step 2: 
      optimizer.zero_grad()

      # step 3: Forward pass 
      pred = model(X_batch)

      # step 4: Loss 
      loss = criterion(pred, y_batch)

      # step 5: Gradient 
      loss.backward()

      # step 6: Update the weight 
      optimizer.step()

      # calculate total loss 
      total_loss += loss.item()

      # count the batch num
      numb_batch += 1 
      
    return total_loss / numb_batch
    
    
