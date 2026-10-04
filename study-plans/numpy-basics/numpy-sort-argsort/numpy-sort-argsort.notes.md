Problems:

Sort a rectangular Python list in ascending order along the supplied axis and report each value's original position within that row or column. Axis 0 sorts each column; axis 1 sorts each row. Return a NumPy float64 array of shape (2, m, n), where m and n are the input row and column counts. Slice 0 contains sorted values; slice 1 contains their zero-based source indices along the selected axis, represented as float64 values.



Break Down:

1. sort the python list in ascending order with supplied axis

1. conver the data into Numpy
2. sort the array in ascending with axis = 1 or 0
2. report each value's original position within that row or cols :

1. sort the index with original position row or cols
3. Return Numpy float of shape (2,m,n) 

1. now we want the shape (2,m,n) so we need to stack both sorted arrays 

1. np.stack

1. arr_sorted
2. index_arr_sorted