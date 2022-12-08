"""
This is a boilerplate pipeline 'data_proc'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import compute_group_size, resolve_na


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=compute_group_size, inputs="train", outputs="train_with_group_size"
            ),
            node(
                func=resolve_na,
                inputs="train_with_group_size",
                outputs="train_preprocessed",
            ),
        ]
    )
