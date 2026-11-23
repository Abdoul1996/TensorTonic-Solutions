import numpy as np

def kfold_split(N: int, k: int, shuffle: bool = True, seed: int = 0) -> list:

    indices = np.arange(N, dtype=int)

    rng = np.random.default_rng(seed)

    if shuffle:
        indices = rng.permutation(indices)

    folds = np.array_split(indices, k)

    splits = []

    for i in range(k):

        val_idx = folds[i].astype(int)

        train_idx = np.concatenate(
            [folds[j] for j in range(k) if j != i]
        ).astype(int)

        splits.append({
            "train_idx": train_idx,
            "val_idx": val_idx
        })

    return splits