Break Down:

1. Compute self-attention using your `multi_head_attention()` function.
2. Add the original input `x` and apply the first `layer_norm()`.
3. Pass the result through `feed_forward()`.
4. Add the residual connection and apply the second `layer_norm()`.