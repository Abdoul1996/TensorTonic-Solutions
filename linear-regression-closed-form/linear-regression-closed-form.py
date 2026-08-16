import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)

    XTX = np.dot(X.T,X)
    XTX_inv = np.linalg.inv(XTX)
    XTy = np.dot(X.T, y)

    w = XTX_inv @ XTy

    return w 