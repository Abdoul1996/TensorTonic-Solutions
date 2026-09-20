Steps:



Here's each stage from the diagram, paired with its formula:

**1. Input batch**


X∈Rn×d,y∈{0,...,K−1}nX \in \mathbb{R}^{n \times d}, \quad y \in \{0, ..., K-1\}^nX∈Rn×d,y∈{0,...,K−1}n

nn n samples, dd d features, KK K classes.

**2. Linear layer**


Z=XW+bZ = XW + bZ=XW+b

W∈Rd×KW \in \mathbb{R}^{d \times K} W∈Rd×K, b∈RKb \in \mathbb{R}^K b∈RK. Output Z∈Rn×KZ \in \mathbb{R}^{n \times K} Z∈Rn×K — one logit per sample per class.

**3. Stability shift**


zi,k←zi,k−max⁡k(zi)z_{i,k} \leftarrow z_{i,k} - \max_k(z_i)zi,k​←zi,k​−kmax​(zi​)

Per-row max subtraction — doesn't change the softmax output, just keeps `exp()` from overflowing.

**4. Softmax**


pi,k=ezi,k∑c=1Kezi,cp_{i,k} = \frac{e^{z_{i,k}}}{\sum_{c=1}^{K} e^{z_{i,c}}}pi,k​=∑c=1K​ezi,c​ezi,k​​

Turns each row of shifted logits into a probability distribution over the KK K classes.

**5. Error signal**


E=P−YonehotE = P - Y_{\text{onehot}}E=P−Yonehot​

This is the gradient of cross-entropy loss with respect to the logits — a clean identity that comes from softmax and cross-entropy's derivatives canceling nicely.

**6. Gradients**


∇WL=1nXTE∇bL=1n∑i=1nEi\nabla_W L = \frac{1}{n} X^T E \qquad \nabla_b L = \frac{1}{n}\sum_{i=1}^{n} E_i∇W​L=n1​XTE∇b​L=n1​i=1∑n​Ei​