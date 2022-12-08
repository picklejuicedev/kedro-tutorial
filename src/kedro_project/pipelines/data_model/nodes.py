"""
This is a boilerplate pipeline 'data_model'
generated using Kedro 0.18.4
"""

from typing import Tuple
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def create_model(df_train: pd.DataFrame) -> Tuple[RandomForestClassifier, list, list]:
    """
    Args:
        df_train (pandas.DataFrame): Dataframe with training data.

    Returns:
        RandomForestClassifier: Trained model.
    """

    target_df = df_train["Transported"]
    df_train = df_train.drop(columns=["PassengerId", "Transported", "Cabin"])

    # split data into training and test data
    X_train, X_test, y_train, y_test = train_test_split(
        df_train, target_df, test_size=0.3, random_state=5981
    )

    # create model
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf, X_test, y_test
