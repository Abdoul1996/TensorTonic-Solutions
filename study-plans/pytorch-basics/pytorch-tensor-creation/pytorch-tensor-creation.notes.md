Problems:



Create a PyTorch float32 tensor of the requested shape. The method is zeros for all zeros, ones for all ones, or full for the supplied fill value. The fill value is ignored for zeros and ones. Return the float32 PyTorch tensor with the requested shape.





Break Down:

1. Create a pyTorch float32 tensor of the requested shape 

1.
2. Methods are zeros, ones, full







Example: 

Input: method = "zeros", shape = [2, 3], value = 0

Output: [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

Explanation: The result has two rows and three columns, all filled with zero.



if the methods == zero:

return torch.zeros(shape)

output: 

[[0,0,0],

[0,0,0]]



if the method == ones:

return torch.ones(shape)

[[1,1,1]

[1,1,1]]









Input: method = "full", shape = [2, 2], value = 7

if the method = ful:

return torch.full(shape)[value]

Output: [[7.0, 7.0], 

              [7.0, 7.0]]