Problem:

Perform one gradient-descent training step on the supplied PyTorch model without an optimizer object.

θnew=θ−η∇θL_θ_new​=_θ_−_η_∇_θ_​_L_

Here, θ_θ_ is a model parameter, L_L_ is the supplied loss function evaluated on the input batch, ∇θL∇_θ_​_L_ is its gradient, and η_η_ is the learning rate. Update every trainable parameter in the supplied model and leave its gradients cleared.

The test panel's data and seed configure an already-supplied float32 linear model with bias and mean-squared-error loss. X and y reach your function as float32 tensors; you do not initialize the model.

Return the batch loss measured before the update as an unrounded Python float.



Break Down:



1. Goal: perform one gradient-descent training step without an optimizer object
2. steps:

1. model.zero_grad()
2. 1. Forward pass

`pred = model(X)`

2. Calculate batch loss

`loss = criterion(pred, y)`

3. Backward pass

`loss.backward()`

4. Manually update parameters

Apply gradient descent using `param.grad`

1. with torch.no_grad():

1. for param in model.parameters():

1. if param.requires_grad:

1. param -= lr * param.grad
2. param.grad.zero()