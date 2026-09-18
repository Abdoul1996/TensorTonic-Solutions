Problems: 

Logistic regression is the foundational algorithm for binary classification. **Given a feature matrix** and **binary labels (0 or 1),** 



the model learns weights and a bias that predict the probability of an input belonging to the positive class.

The model passes a linear combination of features through the **sigmoid function** to output a probability, then uses **binary cross-entropy (BCE)** as the loss function. Train the model using gradient descent.



_σ_(_z_)=1 / 1+ _e_−_z_ (sigmoid function) 



_L_ =  - 1/n ∑​[_y _​log(_y__pred)+(1−_y_) log(1−_y__pred​)]​  binary cross-entropy (BCE) 



dw = _1/n X.T _(_y__pred​−_y_)

db = 1/n sum(y_pred - y) 



w = w - lr * dw 

b = b - lr * db 




### **Requirements**

- Initialize weights _w_ to a zero vector of shape (d,) and bias to 0.0
- For each iteration: 

- compute the linear output z=_Xw_+_b_
- apply the sigmoid: y^=σ(z)_y_^​=_σ_(_z_)
- Compute the gradient of the BCE loss with respect to w and _b_
- Update w and b_b_ using the learning rate
- Return a tuple (weights,bias)(weights,bias) where weights is a list of floats and bias is a float