"""
This is a boilerplate pipeline 'data_model'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_model,
                inputs="train_encoded",
                outputs=["model", "X_test", "y_test"],
            )
        ]
    )
