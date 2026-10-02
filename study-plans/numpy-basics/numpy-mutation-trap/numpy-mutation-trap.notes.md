Problems:

Select the row at the supplied index from a two-dimensional Python list. Preserve its original values and produce a clipped version: values below lo become lo, values above hi become hi, and values inside the bounds remain unchanged. Negative row indices count from the end. Return a NumPy float64 array of shape (2, n), with the original row first and the clipped row second; n is the input column count.



Break down:

1. Select the row at the supplied index from 2D list
2. Preserve its origineal values (views) 

1. Produce a clipped version:

1. low values bec lo
2. val above hi
3. inside remain unchanged