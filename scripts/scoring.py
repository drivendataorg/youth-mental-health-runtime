from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
import typer

CATEGORICAL_COLUMNS = ["InjuryLocationType", "WeaponType1"]


def main(predictions_path: Path, labels_path: Path):
    predictions = pd.read_csv(predictions_path, index_col=0)
    actual = pd.read_csv(labels_path, index_col=0)
    # columns and indices must match
    assert (predictions.columns == actual.columns).all()
    assert (predictions.index == actual.index).all()

    col_f1_scores = []
    for col in predictions.columns:
        if col in CATEGORICAL_COLUMNS:
            col_f1_scores.append(f1_score(actual[col], predictions[col], average="micro"))
        else:
            col_f1_scores.append(f1_score(actual[col], predictions[col], average="binary"))

    print(f"Average F1 score: {np.mean(col_f1_scores):0.4f}")


if __name__ == "__main__":
    typer.run(main)
