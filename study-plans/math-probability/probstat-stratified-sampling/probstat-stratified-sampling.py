from math import floor, sqrt
import numpy as np

def stratified_sample(
    strata_means: list,
    strata_stds: list,
    strata_sizes: list,
    total_sample: int
) -> dict:
    """
    Returns exact allocations, the stratified mean,
    and its standard error.
    """

    # Convert to arrays so element-wise math works
    strata_means = np.asarray(strata_means, dtype=float)
    strata_stds = np.asarray(strata_stds, dtype=float)
    strata_sizes = np.asarray(strata_sizes, dtype=float)

    # 1. Total population
    N = np.sum(strata_sizes)

    # 2. Population weight of each stratum
    weights = strata_sizes / N

    # 3. Ideal proportional allocations
    ideal_allocations = total_sample * weights

    # 4. Floor the allocations
    allocations = [floor(a) for a in ideal_allocations]

    # 5. Find decimal remainders
    remainders = [
        a - floor(a)
        for a in ideal_allocations
    ]

    # 6. Number of observations still unallocated
    leftover = total_sample - sum(allocations)

    # 7. Rank strata by largest remainder
    sorted_indices = sorted(
        range(len(remainders)),
        key=lambda i: remainders[i],
        reverse=True
    )

    # 8. Give leftover observations to largest remainders
    for i in sorted_indices[:leftover]:
        allocations[i] += 1

    allocations = np.asarray(allocations)

    # 9. Stratified mean
    stratified_mean = np.sum(weights * strata_means)

    # 10. Stratified standard error
    stratified_se = sqrt(
        np.sum(
            (weights ** 2) *
            (strata_stds ** 2) /
            allocations
        )
    )

    return {
    "allocations": allocations.tolist(),
    "stratified_mean": round(float(stratified_mean), 4),
    "stratified_se": round(float(stratified_se), 4)
  }