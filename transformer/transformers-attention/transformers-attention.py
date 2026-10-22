import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    # step 1: score 
    query_key_score = torch.matmul(Q, K.transpose(-2,-1))

    # step 2: computing the scaling by dividing d_k which is k weight 

    scalled_score = query_key_score / (K.shape[-1]**0.5) 

    # step 3: Computing softmax 
    softmax_score = torch.softmax(scalled_score, dim=2)

    # step 4: combining softmax score with values 

    scaled_dot_product = torch.matmul(softmax_score, V)

    return scaled_dot_product
