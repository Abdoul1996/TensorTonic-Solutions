import numpy as np

def stratified_split(
    X: list,
    y: list,
    test_size: float = 0.2,
    seed: int = 42
) -> dict:
    """
    Split features and labels while preserving class proportions.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y)

    # Step 1: Identify classes and sample indices
    classes = np.unique(y)
    indices = np.arange(len(y))

    train_part = []
    test_part = []

    rng = np.random.default_rng(seed)

    for cls in classes:
        # Step 2: Find indices belonging to each class
        class_indices = indices[y == cls]

        # Step 3: Shuffle indices within each class
        rng.shuffle(class_indices)

        # Step 4: Calculate test size for each class
        n_class = len(class_indices)
        n_test = round(n_class * test_size)

        # Step 5: Keep at least one sample for training
        if n_class > 1:
            n_test = min(n_test, n_class - 1)

        n_train = n_class - n_test

        # Step 6: Split class indices
        # Step 6: Split class indices
        test_set = class_indices[:n_test]
        train_set = class_indices[n_test:]

        # Step 7: Collect indices
        train_part.append(train_set)
        test_part.append(test_set)

    # Step 8: Combine and sort indices
    train_indices = np.sort(np.concatenate(train_part))
    test_indices = np.sort(np.concatenate(test_part))

    # Step 9: Retrieve features and labels
    X_train = X[train_indices]
    X_test = X[test_indices]

    y_train = y[train_indices]
    y_test = y[test_indices]

    # Step 10: Return results
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test
    }