"""
This is a boilerplate pipeline 'data_report'
generated using Kedro 0.18.4
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def report_model(clf: RandomForestClassifier, X_test: list, y_test: list):
    """
    Args:
        model (sklearn.model): Trained model.
        X_test (list): Test data.
        y_test (list): Test labels.


    """
    print("---------- RandomForest ----------")

    y_pred = clf.predict(X_test)
    print("Accuracy =", "%.2f" % (accuracy_score(y_test, y_pred) * 100), "%")
    print("Precision =", "%.2f" % (precision_score(y_test, y_pred) * 100), "%")
    print("Recall =", "%.2f" % (recall_score(y_test, y_pred) * 100), "%")
    print("F1-Score =", "%.2f" % (f1_score(y_test, y_pred) * 100), "%")
