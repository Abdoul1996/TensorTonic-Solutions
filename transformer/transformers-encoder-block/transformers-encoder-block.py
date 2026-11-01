import numpy as np

def softmax(x, axis=-1):
    """Provided: numerically stable softmax."""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def relu(x: np.ndarray):
  output = np.where(x > 0, x, 0)
  return output

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Returns x normalized over the last axis, then scaled by gamma and shifted by beta.
    """
    mean = np.mean(x, axis=-1, keepdims=True)
    var = np.var(x, axis=-1, keepdims=True)
    normalized = gamma * ((x - mean) / np.sqrt(var + eps)) + beta
    return normalized

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Returns multi-head attention of Q, K, V, projecting them with W_q, W_k, W_v and the merged heads with W_o.
    """

    batch, seq_len, d_model = Q.shape
    d_k = d_model // num_heads
  
    Q_prev = Q @ W_q
    k_prev = K @ W_k
    V_prev = V @ W_v

    # reshaping 
    Q = Q_prev.reshape(batch, seq_len,num_heads, d_k).transpose(0,2,1,3)
    K = k_prev.reshape(batch, seq_len, num_heads, d_k).transpose(0,2,1,3)
    V = V_prev.reshape(batch, seq_len, num_heads, d_k).transpose(0,2,1,3)

    scores = np.matmul(Q,K.transpose(0,1,3,2)) / np.sqrt(d_k)
    attention_weights = softmax(scores, axis=-1)
    attention = attention_weights @ V

    attention = attention.transpose(0,2,1,3).reshape(batch, seq_len, d_model)

    return np.dot(attention, W_o)
    

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Returns the position-wise feed-forward network output with a ReLU hidden layer.
    """
    z1 = np.dot(x, W1) + b1
    hidden = relu(z1)
    output = hidden @ W2 + b2
    return output

def encoder_block(x: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                  W_o: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                  W2: np.ndarray, b2: np.ndarray, gamma1: np.ndarray,
                  beta1: np.ndarray, gamma2: np.ndarray, beta2: np.ndarray,
                  num_heads: int) -> np.ndarray:
    """
    Returns the post-normalized Transformer encoder states.
    """

     # step 1: Multihead Attention 
    attention_output = multi_head_attention(x,x,x, W_q, W_k, W_v,W_o, num_heads)
    residual1 = x + attention_output
    z = layer_norm(residual1,gamma1, beta1, eps=1e-6)

    # Step2 : Feedforward + Norma layer
    residual2 = z + feed_forward(z, W1, b1, W2, b2)
    y = layer_norm(residual2, gamma2, beta2, eps=1e-6)

    return y 
    
    
