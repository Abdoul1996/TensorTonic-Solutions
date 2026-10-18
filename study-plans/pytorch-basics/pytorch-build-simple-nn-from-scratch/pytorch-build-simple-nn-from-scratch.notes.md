Problem:

Build a two-layer PyTorch neural network with one hidden ReLU layer and a linear output layer.



_H_= ReLU (_XW_1T​+_b_1​)

Y=H W2.T+ b2_Y_





Here, _X_ is the input batch, _W_1​ and _b_1​ are the hidden-layer parameters, _H_ is the hidden activation, and _W_2​ and _b_2​ are the output-layer parameters. 



The constructor receives in_features, hidden_size, and out_features. 



The tests use standard PyTorch parameter initialization in network order with seed 42.



The forward method receives a float32 tensor of shape (batch, in_features). Return a float32 PyTorch tensor of shape (batch, out_features), with no output activation.



Breakdown:

1. Architecture: One hidden Linear layer, followed by ReLU, followed by one output Linear layer.

1. nn.Linear(in_features, out_features)
2. nn.ReLU()
3. nn.Linear(out_features)
2. Constructor (`__init__`): Define the layers using `in_features`, `hidden_size`, and `out_features`.

1. self.in_features = in_features
2. self.out_features = out_features
3. Forward pass (`forward`): Pass the input through those layers in the correct order.

1. X - &gt; Linear -&gt; ReLU - &gt; Linear -&gt; Y