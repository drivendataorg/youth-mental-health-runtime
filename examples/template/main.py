"""This is a template for the expected code submission format."""

from pathlib import Path

FEATURES_PATH = Path("data/test_features.csv")
SUBMISSION_PATH = Path("submission.csv")


def main():
    with FEATURES_PATH.open("r") as f:
        # Run inference on the test features
        ...
        pass

    with SUBMISSION_PATH.open("w") as f:
        # Write predictions to the output file
        ...
        pass


if __name__ == "__main__":
    main()
