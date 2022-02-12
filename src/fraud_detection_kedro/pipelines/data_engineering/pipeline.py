"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.17.6
"""

from kedro.pipeline import Pipeline, node
from .nodes import generate_dtypes

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func = generate_dtypes,
            inputs = ['train_transactions'],
            outputs = [dtype],
            name = 'train_dtypes'
        ),
        # node (
        #     func = 
        # )
    ])
