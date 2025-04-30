"""
Evaluation metrics and plotting functions.
"""
from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    """
    Compute metrics on test set.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return {
        "MSE": mse
    }
