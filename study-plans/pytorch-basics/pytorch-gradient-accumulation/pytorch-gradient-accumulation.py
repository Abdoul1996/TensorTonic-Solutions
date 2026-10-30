import torch

def gradient_accumulation(w_init: torch.Tensor, micro_batches: list, lr: float, accum_steps: int) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Returns (final_weights, last_mean_gradient) as float32 tensors.
    """
    # step 1: initialize the weight 
    w = w_init.clone().detach().requires_grad_(True)
    last_mean_gradient = None 

    # step 2: Iterate through the micro_batches 
    for i, (input, t) in enumerate(micro_batches):

      # step 1: forward pass 
      pred = torch.dot(input, w)

      # step 2: compute the loss 
      loss = (pred - t)**2

      # step 4: Backward pass 
      loss.backward()

      # step 5: Update the weight 
      if (i + 1) % accum_steps == 0 or (i+1) == len(micro_batches):
        last_mean_gradient = w.grad.clone() / accum_steps
        
        # update the weights 
        with torch.no_grad():
          w -= lr * last_mean_gradient

        # reset gradients 
        w.grad.zero_()

    return w.detach(), last_mean_gradient.detach()
          
  
