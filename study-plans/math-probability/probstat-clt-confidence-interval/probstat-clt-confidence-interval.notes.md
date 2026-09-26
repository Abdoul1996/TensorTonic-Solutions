### **Requirements**

- Compute the sample mean and sample standard deviation.
- Divide the sample standard deviation by square root n.
- Obtain the two-sided normal critical value from the confidence level.

- alpha = 1 - confidence
- z_critical = norm.ppf(1 - alpha / 2)
- ME = z_critical * SE

       lower_bound = mean - ME

       upper_bound = mean + ME 

- Return the four results in the stated list order.