Problem: 

Use PyTorch autograd to compute the gradient of this scalar function at the values in the supplied PyTorch float32 tensor:

y=∑i=1n(xi3+2xi)_y_=_i_=1∑_n_​(_xi_3​+2_xi_​)

Here, n_n_ is the number of input values, xi_xi_​ is input value i_i_, and y_y_ is the scalar sum. The input is a leaf tensor with gradient tracking initially disabled. Return its gradient as a float32 PyTorch tensor with the same shape and element order.





Break Down: 

1. set up autograd to the values 

1. x.requires_grad = True
2. compute y functions 

1. x = 1 , 2, 3 

y = (1 + 2), (8+4) + (27 + 6) = 3 + 12 + 33 = 48
3. compute gradient 

1. y.backward()
4. return grad

1. x.grad



x = values = [1,2,3] 







_Function: y_=∑​(_x^_3​+2_x_​)



Input: values = [1, 2, 3]



Output: [5.0, 14.0, 29.0]

Explanation: The entries give the local change in the scalar result with respect to the three inputs.