def basic_probability(p_a, p_b, p_a_and_b):
    """
    Returns: [p_union, p_a_complement, p_b_complement, p_a_and_not_b] as a list.
    """

    p_a_u_b = p_a + p_b - p_a_and_b
    p_a_c = 1 - p_a
    p_b_c = 1 - p_b
    p_a_n_b_c = p_a - p_a_and_b

    return [round(p_a_u_b,4), round(p_a_c, 4), round(p_b_c,4), round(p_a_n_b_c,4)]

    