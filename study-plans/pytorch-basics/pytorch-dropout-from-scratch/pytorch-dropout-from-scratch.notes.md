Problem:

Implement Dropout as a PyTorch nn.Module. During training, independently drop each input element with probability p and scale surviving values:

yi= mixi / 1−p​​

Here, xi_xi_​ and yi_yi_​ are input and output elements, and _mi_​ is 0 with probability _p_ and 1 otherwise. Each training call uses a fresh random mask. With p equal to 0, preserve the input; with p equal to 1, return zeros. 



During evaluation, preserve the input for every p.



The constructor receives p, defaulting to 0.5, and forward receives a float32 tensor x. 



The test-panel setting evalMode selects evaluation when true and training when false; it is not an argument to forward.

Return a float32 PyTorch tensor with the same shape as x.\





Break Down :



During Training: 

1. Sample random from uniform or bernoulli
2. Masking: 

1. if value &lt; p -&gt; set element to 0
2. if value &gt;= p -&gt; keep element  and skale it (1 / 1 - p)
3. Edge cases:

1. if p = 0 no element are dropped =&gt; output == input with no scalling
2. if p = 1, all elements are dropped =&gt; output == 0 0 0

Evaluation Mode:

1. Preserve input for every p which menas return X the way its dont drop or scale it