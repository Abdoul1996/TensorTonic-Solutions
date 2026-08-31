import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    rows_before = df.shape[0]
    rows_after = df.drop_duplicates().shape[0]
    cleaned_df = df.drop_duplicates().to_dict('list')

    return [rows_before, rows_after, cleaned_df]
    