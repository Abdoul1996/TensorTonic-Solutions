Problems:

Implement CustomLinear, a PyTorch nn.Module that applies an affine transformation without nn.Linear.

Y=XWT+b

Here, X is the input batch, _W_ is the weight matrix of shape (out_features, in_features), _b_ is the bias vector of length out_features, and _Y_ is the output. 



The constructor receives in_features and out_features. Store learnable float32 parameters named weight and bias. Their initial values are not graded: before the forward call, the runner loads the parameters of an nn.Linear layer initialized with seed 42.



The forward method receives a float32 tensor of shape (batch, in_features). Return a float32 PyTorch tensor of shape (batch, out_features).





Breakdown:



1. Function Y = X * W.T + b
2. custructors:

1. store parameters weight and bias 

1. we need to initializa the weight and bias and set seed = 42
2. w = torch.rand(size of x)
3. b = 0.0
2. create layers here
3. Forward:

1. x as float32
2. call Layers
3. return outputs