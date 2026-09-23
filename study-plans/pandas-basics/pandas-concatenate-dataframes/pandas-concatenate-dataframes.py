import pandas as pd

def concat_dataframes(dfs: list) -> list:
    """
    Returns [shape, data], with shape [rows, columns] and data a dictionary of lists.
    """
    frames = [ pd.DataFrame(d) for d in dfs]

    df_con = pd.concat(frames, axis=0)

    shape = df_con.shape

    return [list(shape), df_con.to_dict('list')]
