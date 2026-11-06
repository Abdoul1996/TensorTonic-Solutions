Problems: 

Compute the mean loss selected by the method using PyTorch tensor operations.

Methods are: mse, cross_entropy and huber loss 



Break down:



1. MSE (regression task) 

1. compute error = prediction - target
2. square_error = (error)^2
3. mean_squared_error
2. Entropy(Classification task)

1. compute logits = z = pred
2. shift z for numerical stability Zstable = z - max(z)
3. exponentiate every scores exp_z = exp(Zstable)
4. deominator = sum(exp(Zstable))
5. probability =  exp^z / denominator
6. probability_class correct probability[target]
7. loss = - log (probability_classcorrect)
3. Huber ( regression task combine mse and abs_mean)

Use for **regression**. It treats small errors like MSE and limits the influence of large errors.

1. Find the error: `pred - target`
2. Take its absolute value.
3. For errors with magnitude at most `delta`, use half the squared error: `0.5 * error**2`.
4. For errors larger than `delta`, use: `delta * (abs(error) - 0.5 * delta)`.
5. Take the mean of the resulting losses.