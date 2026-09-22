My approach 

- Convert `values` and `probabilities` to NumPy arrays with dtype float64
- Compute first_moment = round(sum(values × probabilities), 4)
- Compute second_moment = round(sum(values² × probabilities), 4)
- Compute variance = round(max(0.0, second_moment − first_moment²), 4) — the `max(0.0, ...)` guards against tiny negative values from floating-point rounding right before the sqrt
- Compute std = round(sqrt(variance), 4)
- Return (first_moment, second_moment, variance, std)