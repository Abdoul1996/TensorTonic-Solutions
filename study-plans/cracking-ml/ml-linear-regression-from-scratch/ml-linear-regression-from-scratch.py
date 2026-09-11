import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    
    n_samples, n_features = X.shape

    w = np.zeros(n_features)
    b = 0.0 

    for _ in range(epochs):

        # computer the predictions 
        y_pred = np.dot(X,w) + b 

        # compute the gradient descents 
        errors = y_pred - y 
        dw = 2/n_samples * np.dot(X.T, errors)
        db = 2/n_samples * np.sum(errors)

        # update the parameters
        w -= lr * dw 
        b -= lr * db

    weights = np.round(w, 4)
    bias = np.round(b, 4)

    return (weights, bias)

    
    
