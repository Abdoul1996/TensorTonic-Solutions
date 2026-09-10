**Problem: **

Implement linear regression using gradient descent. Initialize weights to zero and bias to 0, then iteratively update using MSE gradients.



_y_^​=_Xw_+_b_

_L_(_w_,_b_)=_1/n _​∥_Xw_+_b_−_y_∥2 (Loss function MSE) 
### **Requirements**

- Initialize weights to zeros and bias to 0
- Compute predictions as y^=Xw+b
- Update weights and bias using MSE gradients each epoch
- Round all output values to 4 decimal places



Gradient Descents: 

∂_L/dw_​=_2/_n _ ​XT _ *_ _ (_y_^​−_y_),

∂_b_∂_L_​=_2/_n​ * ∑2/_n_​(_y_^​_i_​−_yi_​)



**Approaches: **

1. First we need to initialize w and b to zeros
2. Gradient Descents 

1. Compute predictions as y^ = Xw + b
2. Calculate gradients
3. Update the parameters