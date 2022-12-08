"""
This is a boilerplate pipeline 'data_encode'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import encode_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=encode_data,
                inputs="train_preprocessed",
                outputs="train_encoded",
            )
        ]
    )
