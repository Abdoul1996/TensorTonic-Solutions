import numpy as np

def activation_derivative(name: str, x: list) -> list:
    """
    Returns one analytical derivative for each input value.
    """
    x = np.asarray(x, dtype=float)
    
    # step 1:Defining all the activation functions 
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def tanh(x):
        return np.tanh(x)

    def relu(x):
        return np.where(x<=0, 0.0, 1.0)

    # step 2: Derivated the activation function 

    if name == "sigmoid":
        s = sigmoid(x)
        derivative = (s * (1 - s))
    elif name == "tanh":
        derivative =  1 - (tanh(x)**2)
    elif name == "relu":
        derivative = relu(x)
    else:
        s = sigmoid(x)
        derivative = s + (x * s * (1 - s))

    return derivative.tolist()

    
        