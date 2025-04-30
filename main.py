"""
Main script that orchestrates the full ML pipeline.
"""
from src.config import *
from src.data_loader import load_csv
from src.preprocessing import clean_data, normalize_columns
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model
from src.utils import set_seed

def run_pipeline():
    set_seed(SEED)

    df = load_csv(RAW_DATA_PATH)
    df = clean_data(df)
    df = normalize_columns(df, columns=["feature1", "feature2"])  # adapt to your dataset

    X = df.drop("target", axis=1)
    y = df["target"]

    model = build_model()
    model = train_model(model, X, y)

    metrics = evaluate_model(model, X, y)  # self-evaluation for now
    print("Evaluation metrics:", metrics)

if __name__ == "__main__":
    run_pipeline()
