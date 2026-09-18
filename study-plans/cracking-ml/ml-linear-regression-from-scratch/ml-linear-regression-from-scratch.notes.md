**Problem: **

Implement linear regression using gradient descent. Initialize weights to zero and bias to 0, then iteratively update using MSE gradients.



Goal : To reduce MSE as much as we can 



_y_^​=_Xw_+_b (equation) _

_L_(_w_,_b_)=_1/n _​∥_Xw_+_b_−_y_∥**2 (Loss function MSE) 
### **Requirements**

- Initialize weights to zeros and bias to 0
- Compute predictions as y^=Xw+b
- Update weights and bias using MSE gradients each epoch
- Round all output values to 4 decimal places



Gradient Descents: 

∂_L/dw_​=_2/_n _ ​XT _ *_ _ (_y_^​−_y_),

∂_b_∂_L_​=_2/_n​ * ∑(_y_^​_i_​−_yi_​)



**Approaches: **

1. First we need to initialize w and b to zeros 

1. w is the shape of X columns  to set zeros
2. n is the number os samples X rows
2. Gradient Descents: 

1. Iterate a loop in the epochs 

1. Compute predictions as y^ = Xw + b
2. Calculate gradients: 

1. dw = 2/n _ X.T _ (ypred - y)
2. db = 2/n * sum (ypred - y)
3. Update the parameters using MSE gradients each epoch 

1. w = w - lr * dw
2. b = b - lr 8 db
4. Round all output values to 4 decimal places:

1. w = np.round(w,4)
2. b = np.round(b, 4)
2. Complexity 

1. X (n, d)
2. w (d)
3. X * w (n)
4. y (n)
5. error (n)
6. X.T (d,n)
7. dw (d)
3. Each epock requires matrix vector operation over all n samples and d features so the time complexity is O(nd) per epoch
4. Space complexity:

1. O(n + d)