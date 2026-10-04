Problem:


Given a one-dimensional Python list of angles in radians, compute their sine, cosine, and tangent features. Return a NumPy float64 array of shape (3, n), where n is the number of angles: row 0 contains sine values, row 1 cosine values, and row 2 tangent values.



Break down:

1. given 1-D python lists of angles in randians,

1. convert the list into numpy
2. compute their sin, cosine and tangent features 

1. np.sin(), np.cos(), and np.tan()
3. Return Numpy float of shape (3,n)

1. np.stack([3 values])