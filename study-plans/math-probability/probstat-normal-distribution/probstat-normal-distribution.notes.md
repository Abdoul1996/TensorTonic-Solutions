**Problem statement**
For a normal distribution with mean μ and standard deviation σ, given a value x, compute:

- z-score: z = (x − μ) / σ
- CDF at x
- PDF at x
- Probability that a value lies within one standard deviation of the mean

Return a dictionary with: z_score, cdf, pdf, prob_within_1_std

**Key definitions**

- Z-score: standardizes x — tells you how many standard deviations x is from the mean
- PDF: (1 / (σ√(2π))) · e^(−(x−μ)² / (2σ²))
- CDF: P(X ≤ x) — area under the curve to the left of x
- Quantile function: inverse of the CDF

**Clarified: what are μ, σ, x?**
μ and σ are given parameters of the distribution — not estimated from data. x is the point being evaluated (a single scalar, unless later extended to an array). So np.mean(x) / np.std(x) are NOT needed here.

**CDF — how to compute it**
No elementary closed-form antiderivative exists for the normal PDF, so use the error function:
CDF(x) = ½ · [1 + erf((x − μ) / (σ√2))]
Note: (x − μ)/σ is just the z-score — the erf argument is z/√2.

- `math.erf()` — stdlib, scalar only
- `scipy.stats.norm.cdf()` — handles arrays

**prob_within_1_std — derivation**
Fixed property of the distribution shape: P(μ−σ ≤ X ≤ μ+σ)

- CDF(b) = all area left of b
- CDF(a) = all area left of a
- Subtracting removes the double-counted left region → leaves area between a and b

**prob_within_1_std = CDF(b) − CDF(a)**, where a = μ−σ, b = μ+σ
Equivalently in z-terms: CDF(z=1) − CDF(z=−1)

**Revised approach**

1. Don't compute mean/std from x — μ, σ are given inputs
2. z_score = (x − μ) / σ
3. pdf — plug x, μ, σ into the density formula
4. cdf — use the erf-based formula
5. prob_within_1_std = CDF(μ+σ) − CDF(μ−σ), reusing cdf logic
6. Return dict: z_score, cdf, pdf, prob_within_1_std