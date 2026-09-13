def independence_test(p_a, p_b, p_a_and_b):
    p_a_times_p_b = p_a * p_b

    is_independent = abs(p_a_and_b - p_a_times_p_b) < 1e-9

    return {
        "p_a_times_p_b": round(p_a_times_p_b, 4),
        "is_independent": is_independent
    }