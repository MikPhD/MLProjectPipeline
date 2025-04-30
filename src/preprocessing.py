"""
Feature engineering and preprocessing logic.
"""
def clean_data(df):
    """
    Remove NaNs or irrelevant rows/columns.
    """
    return df.dropna()

def normalize_columns(df, columns):
    """
    Standardize numerical columns to zero mean and unit variance.
    """
    for col in columns:
        df[col] = (df[col] - df[col].mean()) / df[col].std()
    return df
