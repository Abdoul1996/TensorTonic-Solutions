import numpy as np

def knn_classifier(X_train: list, y_train: list, X_test: list, k: int) -> list:
    """
    Returns one predicted label for each test row.
    """
    X_train = np.asarray(X_train, dtype=np.float64)
    X_test = np.asarray(X_test, dtype=np.float64)
    y_train = np.asarray(y_train)

    predictions = []

    for rows in X_test:
        diffs = X_train - rows
        distance = np.sqrt(np.sum(diffs**2, axis=1))
        sorted_indices = np.argsort(distance, kind='stable')
        k_nearest_indicess = sorted_indices[:k]
        k_nearest_labels = y_train[k_nearest_indicess]
        values, counts = np.unique(k_nearest_labels, return_counts=True)
        best_index = np.argmax(counts)
        predicted_label = int(values[best_index])
        predictions.append(predicted_label)

    return predictions
