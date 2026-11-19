Break Down:



1. We need to calculate boostrap of all the sample mean 

1. firstly iterate through the n_boostrap, 

1. each iteration we take a sample and compute the mean, and store boostrap_mean until the loop is done
2. Then we need to compute the mean

1. Then we take the average of the mean of all the means from boostrap_mean. which is our estimator

1. **Make the CI step concrete.** Set α=(1−c)/2_α_=(1−_c_)/2, where c_c_ is `ci`. Then `lower` is the α_α_ quantile and `upper` is the 1−α1−_α_ quantile **of your B*****B***** bootstrap means**, not of the original data.