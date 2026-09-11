import numpy as np

def logistic_regression(X, y, lr=0.01, n_iters=1000):
    """
    Returns:
        tuple: (weights, bias) where weights is a list and bias is a float
    """
    X =  np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    n_samples, n_features = X.shape

    w = np.zeros(n_features)
    b = 0.0 

    for _ in range(n_iters):
        z = np.dot(X, w) + b 
        
        y_pred = 1 / (1 + np.exp(-z)) # sigmoid function
        
        loss = - (1/n_samples * np.sum(y * np.log(y_pred)) + (1-y) * np.log(1-y_pred))
        
        dw = 1/n_samples * np.dot(X.T, y_pred - y)
        db = 1/n_samples * np.sum(y_pred - y)

        w -= lr * dw
        b -= lr * db

    weights = np.round(w, 4)
    bias = np.round(b, 4)

    return (weights, bias)
