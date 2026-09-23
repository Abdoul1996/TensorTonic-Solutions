import pandas as pd

def cross_tab(data: dict, row_col: str, col_col: str) -> dict:
    """
    Returns a dictionary from column labels to dictionaries of row labels and integer counts.
    """

    df = pd.DataFrame(data)

    output = pd.crosstab(df[row_col], df[col_col])

    return output.to_dict()

    
    
    
