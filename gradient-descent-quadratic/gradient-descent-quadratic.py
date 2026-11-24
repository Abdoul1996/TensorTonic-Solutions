def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    
    # Step 1: Initialize current position
    x = x0

    # Step 2: Iterate
    for i in range(steps):

        # Step 3: Compute derivative
        gradient = 2 * a * x + b 

        # Step 4: Update x
        x = x - lr * gradient

    # Step 5: Return final position
    return x