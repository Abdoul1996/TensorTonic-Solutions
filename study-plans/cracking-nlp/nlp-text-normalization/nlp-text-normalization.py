import re

def text_normalize(text: str, operations: list) -> str:
    """
    Returns the normalized string.
    """
    for operation in operations:
      if operation == "lowercase":
        text = text.lower()
      elif operation == "strip":
        text = text.strip()
      elif operation == "remove_digits":
        text = re.sub(r"\d","", text)
      elif operation == "remove_punctuation":
        text = re.sub(r"[^\w\s]|_","", text)
      elif operation == "collapse_whitespace":
        text = re.sub(r"\s+"," ", text)
    return text 
