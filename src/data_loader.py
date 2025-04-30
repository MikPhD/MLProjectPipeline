"""
Functions for loading datasets from various formats.
"""
import pandas as pd

def load_csv(path):
    """
    Load dataset from a CSV file.
    """
    return pd.read_csv(path)

def load_hdf5(path):
    """
    Placeholder for loading data from HDF5 files.
    """
    pass  # implement if needed
