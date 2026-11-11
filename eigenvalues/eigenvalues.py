import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.array(matrix, dtype=float)

    # step 1: Compute the eigenvalues using np.linalg.eigenvalues()
    eigenvalues = np.linalg.eigvals(matrix)
    # step 2: convet to real number 
    eigenvalues = np.real_if_close(eigenvalues).real
  
    # step 3: sort the eigenvalues
    eigenvalues = np.sort(eigenvalues)
    return eigenvalues