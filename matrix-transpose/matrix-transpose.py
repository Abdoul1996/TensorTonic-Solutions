import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A, dtype=float)

    # Step 1: Find col and rows 
    rows, cols = A.shape

    # step 2: create a new matrix with shape rows and cols 
    matrix = np.zeros((cols, rows))

    # Iterathrough and swap index 
    for i in range(rows):
      for j in range(cols):
        matrix[j, i] = A[i,j]

    return matrix