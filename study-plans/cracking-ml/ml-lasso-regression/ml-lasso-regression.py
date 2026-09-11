def lasso_regression(X, y, lr, epochs, alpha):
    """
    Perform Lasso Regression using gradient descent with L1 subgradient.
    Returns: tuple of (weights_list, bias_float)
    """
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    n,d = X.shape
    
    w = np.zeros(d)
    b = 0.0 

    for _ in range(epochs):

        # compute predictions 
        y_pred = np.dot(X, w) + b 

        # compute the error 
        error = y_pred - y 

        # compute the gradients 
        dw = 2/n * np.dot(X.T, error) + alpha * np.sign(w)
        db = 2/n * np.sum(error)

        w -= lr * dw 
        b -= lr * db 

    weights = np.round(w, 4)
    bias = np.round(b, 4)

    return (weights, bias)