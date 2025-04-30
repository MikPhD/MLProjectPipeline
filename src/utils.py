"""
General-purpose utilities: logging, seeds, timers, etc.
"""
import random
import numpy as np
import logging

def set_seed(seed):
    """
    Set random seed for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)

def setup_logger(log_file_path):
    """
    Set up a logger that writes to file.
    """
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    return logging.getLogger()
