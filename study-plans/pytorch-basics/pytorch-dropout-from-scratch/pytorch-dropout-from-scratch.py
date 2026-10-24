import torch
import torch.nn as nn

class Dropout(nn.Module):
    def __init__(self, p: float = 0.5):
        super().__init__()
        self.p = p 

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor with the same shape as x.
        """
        x = x.to(dtype=torch.float32)
        # checking mode of the model 
        if not self.training:
          return x 

        # Handling Edge cases 
        if self.p == 0:
          return x
        if self.p == 1:
          return torch.zeros_like(x)

        # Training dropout 

        # step 1 : sample random using bernoulli normalization 
        random_values = torch.rand_like(x)

        # step 2: creating masking if random_va >= p boolean  
        mask = random_values >= self.p 

        # step 3: applying the dropout 
        output = torch.where(mask, x, 0)

        # step 4: scalling the output 
        scalling_outp = output / (1 - self.p)

        return scalling_outp

        
        

        
