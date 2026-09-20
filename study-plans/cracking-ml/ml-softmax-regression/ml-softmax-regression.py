import numpy as np

def softmax_regression(X: list, y: list, num_classes: int, lr: float, n_iters: int) -> tuple:
    """
    Returns the fitted weight matrix and bias vector.
    """

    # Step 1: Setting up 
    X = np.asarray(X, dtype='float64')
    y = np.asarray(y, dtype='int64')

    n, d = X.shape
    k = num_classes

    w = np.zeros((d,k), dtype='float64')
    b = np.zeros(k)

    y_onehot = np.eye(k, dtype='float64') [y]

    # Iteration Loop 
    for _ in range(n_iters):

        # step 1: compute logits
        logits = np.dot(X, w) + b

        # step 2: Stability shift 
        logits -= np.max(logits, axis=1, keepdims=True)

        # step 3: Softmax Probabilities  
        probabilities = np.exp(logits) / np.sum(np.exp(logits), axis=1, keepdims=True)

        # step 4 : Error Signal 
        Error = probabilities - y_onehot

        # step 5: Gradient descent 
        dw = 1/n * np.dot(X.T, Error)
        db = 1/n * np.sum(Error, axis=0)

        # step 6 : Parameters Updates 
        w -= lr * dw
        b -= lr * db 

    weight = np.round(w, 4)
    bias = np.round(b, 4 )

    return (weight, bias)
        
    
    
