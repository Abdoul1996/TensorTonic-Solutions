import pandas as pd

def multi_agg(data: dict, group_col: str, value_col: str, funcs: list) -> dict:
    """
    Returns a dictionary from function names to dictionaries of group aggregates.
    """
    df = pd.DataFrame(data)
    grouped = df.groupby(group_col)[value_col]

    return {
        func: grouped.agg(func).to_dict()
        for func in funcs

    }
