Problem:

Implement scaled dot-product attention from the Transformer.

Attention⁡(Q,K,V)= softmax⁡ ⁣(Q*K.T / sqrt(d_k))V

Here, Q contains queries, K contains keys, V contains values, and d_k is the key width. 



Apply softmax along the key-position axis.



 Return a PyTorch float32 tensor with shape (batch, query_length, value_width).



Break down:

1. Let's calculate Q and K.T scores
2. compute the scaling by dividing d_k in the score which we can access it by key d_k = k.shape[-1] which is the dimensional
3. weight = Apply softmax = e^scalled / sum(e^scalled) # produce attention weight
4. scalled dot product = weight * v combine value vectors