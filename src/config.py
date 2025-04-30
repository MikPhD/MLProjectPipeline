"""
Global configuration module.
Defines project-wide constants and hyperparameters.
"""

# Paths
DATA_DIR = "data/"
RAW_DATA_PATH = DATA_DIR + "raw/data.csv"
PROCESSED_DATA_PATH = DATA_DIR + "processed/data_processed.csv"
MODEL_DIR = "models/"
OUTPUT_DIR = "outputs/"
LOG_DIR = "logs/"

# Reproducibility
SEED = 42

# Training parameters
BATCH_SIZE = 32
LEARNING_RATE = 0.001
EPOCHS = 50
