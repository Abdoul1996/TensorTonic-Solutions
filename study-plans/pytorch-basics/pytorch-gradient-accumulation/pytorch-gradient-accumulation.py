import torch

def gradient_accumulation(w_init: torch.Tensor, micro_batches: list, lr: float, accum_steps: int) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Returns (final_weights, last_mean_gradient) as float32 tensors.
    """
    w = w_init.clone().detach().requires_grad_(True)
    last_mean_grad = None 

    for i, (x,y) in enumerate(micro_batches):
      pred = torch.dot(x,w)
      loss = (pred - y)**2
      loss.backward()

      if (i+1) % accum_steps == 0 or (i+1) == len(micro_batches):
        last_mean_grad = w.grad.clone() / accum_steps

        with torch.no_grad():
          w -= lr * last_mean_grad

        w.grad.zero_()

    return w.detach(), last_mean_grad.detach()
        
