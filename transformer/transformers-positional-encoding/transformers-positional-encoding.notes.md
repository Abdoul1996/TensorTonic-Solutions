Problems:

Implement the fixed sinusoidal positional encoding from the Transformer.

Here, pos is a zero-based sequence position, i indexes a sine-cosine pair, and d_model is the model width. Return a NumPy float64 array with shape (seq_length, d_model).



Break Down:



 The algorithm needs three main steps

1. Initialize: Create an empty NumPy array of shape `(seq_length, d_model)` with dtype `float64`.
2. Calculate: Visit each position and dimension, 

1. Calculate the appropriate angle,
2. Apply sine for even dimensions or cosine for odd dimensions.
3. Return: Return the completed positional encoding matrix.