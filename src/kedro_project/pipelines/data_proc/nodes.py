"""
This is a boilerplate pipeline 'data_proc'
generated using Kedro 0.18.4
"""

import pandas as pd


def compute_group_size(df_train: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        df_train (pandas.DataFrame): Dataframe with training data.

    Returns:
        pandas.DataFrame: Dataframe with training data and group size.

    """
    split_df = df_train["PassengerId"].str.split(pat="_", expand=True)
    alone = split_df[0].value_counts()
    split_df = split_df.merge(alone.rename("groupSize"), left_on=0, right_index=True)
    df_train["groupSize"] = split_df["groupSize"]
    return df_train


def resolve_na(df_train: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        df_train (pandas.DataFrame): Dataframe with training data.

    Returns:
        pandas.DataFrame: Dataframe with training data and filled na.

    """
    # deal with Nan: fill costs with 0.0, remove all others
    cols = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
    df_train[cols] = df_train[cols].fillna(0.0)

    df_train = df_train.dropna()
    return df_train
