"""
This is a boilerplate pipeline 'data_encode'
generated using Kedro 0.18.4
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_data(df_train: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        df_train (pandas.DataFrame): Dataframe with training data.

    Returns:
        pandas.DataFrame: Dataframe with training data and encoded features.
    """
    # convert strings to enums using labelencoder
    cols = ["HomePlanet", "CryoSleep", "Destination", "VIP"]
    df_train[cols] = df_train[cols].apply(LabelEncoder().fit_transform)

    # drop name column
    df_train = df_train.drop(columns=["Name"])
    return df_train
