Problem:

Normalize a matrix by an L1, L2, or maximum norm. Compute the selected norm over columns when axis=0, rows when axis=1, or the complete matrix when axis=None.



Divide every value by the norm of its selected slice. A zero-norm slice remains zero. Return a NumPy array with the same shape as the matrix.



Break Down:



ROW

1. l1 = np.abs(matrix) / np.sum(matrix, axis=1, keepdim=True)
2. l2 = matrix / np.sum(np.sqrt(matrix), axis=1, keepdim=True)
3. max = matrix / np.max(matrix, axis=1, keepdim=True)

COL 

1. l1 = np.abs(matrix) / np.sum(matrix, axis=0, keepdim=True)
2. l2 = matrix / np.sum(np.sqrt(matrix), axis=0, keepdim=True)
3. max = matrix / np.max(matrix, axis=1, keepdim=True)



For edge cases:

if its zero, we remain the norm zero