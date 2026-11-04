import numpy as np 
def pad_and_truncate(sequences: list, max_length: int, pad_value: int = 0) -> list:
    """
    Returns one integer list of length max_length per input sequence.
    """

    result = []
    for seq in sequences:

      if len(seq) < max_length:
        missing = max_length - len(seq)
        pad = [pad_value] * missing
        processed = seq + pad

      else:
        processed = seq[:max_length]

      result.append(processed)

    return result
        
        
    