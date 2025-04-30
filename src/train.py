"""
Training logic for fitting models.
"""
def train_model(model, X_train, y_train):
    """
    Fit model to training data.
    """
    model.fit(X_train, y_train)
    return model
