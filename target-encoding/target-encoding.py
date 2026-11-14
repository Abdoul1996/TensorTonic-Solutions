import numpy as np 
def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    group = {}
    encoded = {}
    result = []

    # Step 1: Merge into dict categories and target
    for i in range(len(categories)):
      category = categories[i]
      target = targets[i]

      if category not in group:
        group[category] = []
      group[category].append(target)

    for key, value in group.items():
      mean = np.mean(value)
      encoded[key] = mean 

    for word in categories:
      result.append(encoded[word])

    return result

    