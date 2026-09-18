import numpy as np

def ridge_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """

    X = np.asarray(X, dtype='float64')
    y = np.asarray(y, dtype='float64')

    n, d = X.shape

    w = np.zeros(d)
    b = 0.0 

    for _ in range(epochs):
        y_pred = np.dot(X, w) + b 

        error = y_pred - y 

        dw = 2/n * np.dot(X.T, error)  + 2 * alpha * w
        db = 2/n * np.sum(error)

        w -= lr * dw
        b -= lr * db 

    weight = np.round(w, 4)
    bias = np.round(b, 4)

    return (weight, bias)
    
