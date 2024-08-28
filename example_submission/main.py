"""This is an example of a valid, functional submission."""

from pathlib import Path

import pandas as pd

SUBMISSION_PATH = Path("submission.csv")
FEATURES_PATH = Path("data/test_features.csv")
SUBMISSION_FORMAT_PATH = Path("data/submission_format.csv")


def generate_predictions(features: pd.DataFrame, submission_format: pd.DataFrame) -> pd.DataFrame:
    """Generate some bad predictions. You can make this function better!"""
    predictions = pd.DataFrame(index=submission_format.index, columns=submission_format.columns)
    # Predict 1 for every binary variable
    for col in predictions.columns:
        predictions[col] = 1
    # Predict the same value across rows for each categorical variable
    predictions["InjuryLocationType"] = 11
    predictions["WeaponType1"] = 6

    return predictions


def main():
    features = pd.read_csv(FEATURES_PATH, index_col=0)
    print(f"Loaded test features of shape {features.shape}")

    submission_format = pd.read_csv(SUBMISSION_FORMAT_PATH, index_col=0)
    print(f"Loaded submission format of shape: {submission_format.shape}")

    # Generate predictions
    predictions = generate_predictions(features, submission_format)
    print(f"Saving predictions of shape {predictions.shape} to {SUBMISSION_PATH}")
    predictions.to_csv(SUBMISSION_PATH, index=True)


if __name__ == "__main__":
    main()
