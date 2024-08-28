from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
import typer


def average_f1(predictions: pd.DataFrame, labels: pd.DataFrame):
    """Score a set of predictions using the competition metric. F1 is averaged
    across all target variables. For categorical variables, micro-averaged
    F1 score is used.

    Args:
        predictions (pd.DataFrame): Dataframe of predictions, with one column
            for each target variable. The index should be the uid.
        labels (pd.DataFrame): Dataframe of ground truth values, with one column
            for each target variable. The index should be the uid.
    """
    # Check that there are 23 target variables
    assert predictions.shape[1] == 23

    # Check that column order and row order are the same
    assert (predictions.columns == labels.columns).all()
    assert (predictions.index == labels.index).all()

    # All values should be integers
    assert (predictions.dtypes == int).all()

    CATEGORICAL_VARS = ["InjuryLocationType", "WeaponType1"]
    BINARY_VARS = np.setdiff1d(labels.columns, CATEGORICAL_VARS)

    # Calculate F1 score averaged across binary variables
    binary_f1 = f1_score(
        labels[BINARY_VARS],
        predictions[BINARY_VARS],
        average="macro",
    )
    f1s = [binary_f1]

    # Calculate F1 score for each categorical variable
    for cat_col in CATEGORICAL_VARS:
        f1s.append(f1_score(labels[cat_col], predictions[cat_col], average="micro"))

    return np.average(f1s, weights=[len(BINARY_VARS), 1, 1])


def main(predictions_path: Path, labels_path: Path):
    predictions = pd.read_csv(predictions_path, index_col="uid")
    labels = pd.read_csv(labels_path, index_col="uid")

    score = average_f1(predictions, labels)
    print(f"Variable-averaged F1 score: {score:.4f}")


if __name__ == "__main__":
    typer.run(main)
