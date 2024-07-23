import importlib

import pytest

packages = [
    "numpy",
    "pandas",
    "scipy",
    "sklearn",
]


@pytest.mark.parametrize("package_name", packages, ids=packages)
def test_import(package_name):
    """Test that certain dependencies are importable."""
    importlib.import_module(package_name)
