from collections import defaultdict
import sys
import warnings
from os import PathLike
from pathlib import Path

import yaml


def main(package_list_path: PathLike):
    """Check the environment

    Args:
        package_list_path (PathLike): Path to the output of `pixi list --json`
    """
    with Path(package_list_path).open("r") as fp:
        packages = yaml.safe_load(fp)

    package_count = defaultdict(lambda: 0)
    package_kind_count = defaultdict(lambda: 0)
    for package in packages:
        package_count[package["name"]] += 1
        package_kind_count[package["kind"]] += 1
    repeated_deps = [
        package_name for package_name in package_count if package_count[package_name] > 1
    ]

    if len(repeated_deps):
        warnings.warn(f"There are duplicate packages in the environment: {repeated_deps}")
    else:
        print(f"Lockfile {package_list_path} passed. Package kinds: {dict(package_kind_count)}")


if __name__ == "__main__":
    main(sys.argv[1])
