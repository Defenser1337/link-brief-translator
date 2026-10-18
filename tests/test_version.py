"""Smoke tests for the package itself."""

import lbt


def test_package_version() -> None:
    assert lbt.__version__ == "0.1.0"
