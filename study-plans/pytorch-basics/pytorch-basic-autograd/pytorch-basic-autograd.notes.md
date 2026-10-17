Problem: 

Use PyTorch autograd to compute the gradient of this scalar function at the values in the supplied PyTorch float32 tensor:

y=∑i=1n(xi3+2xi)_y_=_i_=1∑_n_​(_xi_3​+2_xi_​)

Here, n_n_ is the number of input values, xi_xi_​ is input value i_i_, and y_y_ is the scalar sum. The input is a leaf tensor with gradient tracking initially disabled. Return its gradient as a float32 PyTorch tensor with the same shape and element order.





Break Down: 

1. set up autograd to the values
2. compute y functions
3. compute gradient
4. return grad