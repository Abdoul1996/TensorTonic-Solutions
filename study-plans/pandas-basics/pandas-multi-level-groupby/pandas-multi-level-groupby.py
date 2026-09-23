import pandas as pd

def multi_groupby(data: dict, group_cols: list, value_col: str, aggfunc: str) -> dict:
    """
    Returns a dictionary of lists for the grouping columns and aggregated value column.
    """
    df = pd.DataFrame(data)

    group_data = df.groupby(group_cols)[value_col]

    return group_data.agg(aggfunc).reset_index().to_dict('list')
