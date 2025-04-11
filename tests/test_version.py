import importlib
import re

import pytest

SEMVER_PATTERN = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)
"""Defined at: https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string"""


@pytest.mark.parametrize("package", ["moltrack"])
def test_has_version(package: str) -> None:
    """Ensures that module has a valid SemVer version."""
    pkg = importlib.import_module(package)

    assert hasattr(pkg, "__version__")
    assert SEMVER_PATTERN.fullmatch(pkg.__version__)
