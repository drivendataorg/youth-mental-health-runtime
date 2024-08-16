"""This is an example of a valid, functional submission."""

from loguru import logger
from pathlib import Path

import pandas as pd

SUBMISSION_PATH = Path("submission.csv")
FEATURES_PATH = Path("data/test_features.csv")
SUBMISSION_FORMAT_PATH = Path("data/submission_format.csv")


def main():
    features = pd.read_csv(FEATURES_PATH)
    logger.info(f"Loaded test features of shape {features.shape}")

    sub_format = pd.read_csv(SUBMISSION_FORMAT_PATH)

    predictions = pd.DataFrame({"uid": features.uid})
    for col in sub_format.columns:
        predictions[col] = 0
    predictions["WeaponType1"] = "Unknown"
    predictions["InjuryLocationType"] = "Other"
    logger.info(f"Saving predictions of shape {predictions.shape} to {SUBMISSION_PATH}")

    predictions.to_csv(SUBMISSION_PATH, index=False)


if __name__ == "__main__":
    main()
