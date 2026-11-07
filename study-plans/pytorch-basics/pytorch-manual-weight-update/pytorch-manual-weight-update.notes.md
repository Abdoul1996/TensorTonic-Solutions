Problem:

Perform one gradient-descent training step on the supplied PyTorch model without an optimizer object.

θnew=θ−η∇θL_θ_new​=_θ_−_η_∇_θ_​_L_

Here, θ_θ_ is a model parameter, L_L_ is the supplied loss function evaluated on the input batch, ∇θL∇_θ_​_L_ is its gradient, and η_η_ is the learning rate. Update every trainable parameter in the supplied model and leave its gradients cleared.

The test panel's data and seed configure an already-supplied float32 linear model with bias and mean-squared-error loss. X and y reach your function as float32 tensors; you do not initialize the model.

Return the batch loss measured before the update as an unrounded Python float.



Break Down:



1. Goal: perform one gradient-descent training step without an optimizer object
2. steps:

1. Initialize the model parameters 

1. weight = nn.Parameter(torch.zeros(x.shape))
2. bias = nn.Parameter(torch.zeros(x.shape[0])
3. weight = torch.tensor(weight, requires_grad = True)
4. Iteratrhought the x im assuming here im not sure how to get the batch, the reason i choose x is (N,D) N is the batch i think im not sure
5. 
6. Forward pass 

1. pred = model(x)
2. loss = criterion(pred, y)
3. loss.backward
4. im struggling optimizer, and how to update the weight, i understand the concept but im struggling how to put together
7. we are returning batch loss im not sure if that meant to be w.grad