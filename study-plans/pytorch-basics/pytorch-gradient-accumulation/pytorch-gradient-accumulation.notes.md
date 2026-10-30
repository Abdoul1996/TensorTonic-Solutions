Problem:

Train a weight vector using gradient accumulation over consecutive groups of micro-batches. Each micro-batch contains an input vector and a scalar target, with squared-error loss:

L=(wTx−t)2

Here, w_w_ is the current weight vector, x_x_ is the micro-batch input vector, t_t_ is its target, and L_L_ is its loss. 



All micro-batches in a group use the same weights. Each group produces one gradient-descent update using its mean gradient and the supplied learning rate. The group size is accum_steps, and no gradients carry between groups.



The initial weights and input vectors are float32 PyTorch tensors; each target is a Python float. Return a tuple of two float32 PyTorch tensors: the final weight vector, then the mean gradient used in the last update. Both have the same shape as the initial weights.



Breakdown:

Goal: Train weight vector using gradient accumulation over consecutive groups of micro batches



Parameters:

- w_init : initial model weights
- micro_batches : list of (input vector, target) pairs
- lr
- accum_Steps :  number of micro batches before updating the weight



Each Micro batch contains:

- Input : x
- target: t

1. Inittialize the weight
2. Iterate micro batch:

1. Initialize the weights
2.