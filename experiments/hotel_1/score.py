def count_labels(y):
    output = set()
    for i, yi in enumerate(y):
        for label in yi:
            output.add((i, label))
    return output


def multilabel_f1_score(y_true, y_pred):
    labels_true = count_labels(y_true)
    labels_pred = count_labels(y_pred)
    if len(labels_true) == 0 and len(labels_pred) == 0:
        return 1
    if len(labels_pred) == 0:
        return 0
    p = len(labels_pred.intersection(labels_true)) / len(labels_pred)
    r = len(labels_pred.intersection(labels_true)) / len(labels_true)
    if p == 0:
        return 0
    f1 = (2 * p * r) / (p + r)
    return f1


def multilabel_score(y_true, y_pred):
    labels_true = count_labels(y_true)
    labels_pred = count_labels(y_pred)
    if len(labels_true) == 0 and len(labels_pred) == 0:
        return 1
    if len(labels_pred) == 0:
        return 0
    p = len(labels_pred.intersection(labels_true)) / len(labels_pred)
    r = len(labels_pred.intersection(labels_true)) / len(labels_true)
    if p == 0:
        return 0
    f1 = (2 * p * r) / (p + r)
    score = {
        "precision": p,
        "recall": r,
        "f1": f1
    }
    return score
