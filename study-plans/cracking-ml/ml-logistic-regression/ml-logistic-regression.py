import numpy as np

def logistic_regression(X: list, y: list, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """

    X = np.asarray(X, dtype='float64')
    y = np.asarray(y, dtype='float64')

    n, d = X.shape

    w = np.zeros(d)
    b = 0.0 

    for _ in range(n_iters):
        z = np.dot(X, w) + b 
        y_prob = 1 / (1 + np.exp(-z))

        error = y_prob - y 

        dw = 1/n * np.dot(X.T, error)
        db = 1/n * np.sum(error)

        w -= lr * dw
        b -= lr * db

    weights = np.round(w, 4)
    bias = np.round(b, 4)

    return (weights, bias)
    
