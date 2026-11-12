import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    A = np.asarray(A, dtype=float)
    n = A.shape[0]

    I = np.eye(n)
    aug = np.hstack((A, I))

    for col in range(n):
        # Step 1: Find pivot row
        pivot_row = col + np.argmax(np.abs(aug[col:, col]))

        # Step 2: Check if pivot is zero
        if np.isclose(aug[pivot_row, col], 0):
            return None

        # Step 3: Swap rows
        aug[[col, pivot_row]] = aug[[pivot_row, col]]

        # Step 4: Normalize pivot row
        aug[col] = aug[col] / aug[col, col]

        # Step 5: Eliminate other rows
        for row in range(n):
            if row != col:
                factor = aug[row, col]
                aug[row] -= factor * aug[col]

    return aug[:, n:]