"""
Model definition.
Replace or extend for scientific modeling needs.
"""
from sklearn.linear_model import LinearRegression

def build_model(model_type="linear", **kwargs):
    """
    Build and return a model object.
    """
    if model_type == "linear":
        return LinearRegression(**kwargs)
    else:
        raise NotImplementedError(f"Model '{model_type}' is not supported.")
