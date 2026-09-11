def ridge_regression(X, y, lr, epochs, alpha):
    """
    Perform ridge regression using gradient descent.
    Returns: tuple of (weights_list, bias)
    """

    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    n,d = X.shape

    w = np.zeros(d)
    b = 0.0 

    for _ in range(epochs):
        y_pred = np.dot(X, w) + b 
        error = y_pred - y 

        #compute the gradient descents 
        dw = 2/n * np.dot(X.T, error) + 2 * alpha * w
        db = 2/n * np.sum(error)

        w -= lr * dw
        b -= lr * db 

    weights = np.round(w, 4)
    bias = np.round(b, 4)
    return (weights, bias)

        