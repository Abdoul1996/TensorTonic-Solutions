import pandas as pd

def merge_dataframes(left: dict, right: dict, on: str, how: str) -> dict:
    """
    Returns a dictionary of merged column lists, with NaN for unmatched cells.
    """
    df_left = pd.DataFrame(left)
    df_right = pd.DataFrame(right)

    df = pd.merge(df_left, df_right, on=on, how=how)

    return df.to_dict('list')