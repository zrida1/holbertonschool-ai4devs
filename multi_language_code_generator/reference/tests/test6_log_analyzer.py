import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_parse_empty_raises():
    with pytest.raises(ValueError):
        LogAnalyzer().parse_line("")