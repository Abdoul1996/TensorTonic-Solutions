Problem:

MHA(_Q_,_K_,_V_)=Concat(_head_1​,…,_headh_​)_WO_

Here, 



h is num_heads and (d_k=d_{model}/h). 



The supplied projection matrices combine every head in one model-width matrix. Return a NumPy float64 array with shape (batch, query_length, d_model).



Break Down :

Q = Q * W_q

K = K * W_k 

V = V * W_v 



d_k = d_model / h 









1. Let's calculate Q and K.T scores
2. compute the scaling by dividing d_k in the score which we can access it by key d_k = k.shape[-1] which is the dimensional
3. weight = Apply softmax = e^scalled / sum(e^scalled) # produce attention weight
4. scalled dot product = weight * v combine value vectors