import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0 

    for _ in range(epochs):
        y_pred = np.dot(X, w) + b # compute the predictions 
        # Computing the gradients 
        dw = 2.0/n_samples * np.dot(X.T,(y_pred - y))
        db = 2.0/n_samples * np.sum(y_pred - y)
        #  updates the parameters 
        w = w - lr  * dw
        b = b - lr * db
    weights = np.round(w,4)
    bias = np.round(b,4)

    return (weights, bias)
        
        
        
        

        
        

    
    
