"""
Useful decorators for profiling, logging, timing, and debugging.
"""
import time
import functools
import logging
import tracemalloc

def timing(func):
    """Prints the execution time of the decorated function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} executed in {end - start:.4f} sec")
        return result
    return wrapper

def log_execution(logger=None):
    """Logs function entry and exit."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log = logger or logging.getLogger(func.__module__)
            log.info(f"Entering: {func.__name__}")
            result = func(*args, **kwargs)
            log.info(f"Exiting: {func.__name__}")
            return result
        return wrapper
    return decorator

def catch_errors(func):
    """Catches and logs exceptions without stopping execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR in {func.__name__}]: {e}")
            return None
    return wrapper

def profile_memory(func):
    """Prints memory usage of the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        print(f"[MEMORY] {func.__name__}: Current = {current / 10**6:.2f}MB; Peak = {peak / 10**6:.2f}MB")
        tracemalloc.stop()
        return result
    return wrapper
