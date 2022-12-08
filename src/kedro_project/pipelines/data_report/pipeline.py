"""
This is a boilerplate pipeline 'data_report'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import report_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=report_model,
                inputs=["model", "X_test", "y_test"],
                outputs=None,
            )
        ]
    )
