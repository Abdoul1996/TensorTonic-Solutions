The important pieces are:

- nn = number of observations
- xix_i = each individual value
- xˉ\bar{x} = sample mean
- ss = **sample standard deviation**, so use the n−1n-1 version
- skewness uses the **3rd power**
- kurtosis uses the **4th power**

So before coding, your mental algorithm should be:

1. get `n`
2. calculate sample mean
3. calculate sample standard deviation
4. compute each standardized deviation

xi−xˉs\frac{x_i-\bar{x}}{s}
5. cube them and sum for skewness
6. raise them to the 4th power and sum for kurtosis
7. apply the correction terms from the formulas
8. classify the result



classification:

skewness distribution

if g1 &gt; 0.5:

    skew_interpretation = "right-skewed"

elif g1 &lt; -0.5:

    skew_interpretation = "left-skewed"

else:

    skew_interpretation = "approximately symmetric"



part ii : kurtosis the tail weights 

if g2 &gt; 1:

    kurtosis_interpretation = "leptokurtic"

elif g2 &lt; -1:

    kurtosis_interpretation = "platykurtic"

else:

    kurtosis_interpretation = "mesokurtic"