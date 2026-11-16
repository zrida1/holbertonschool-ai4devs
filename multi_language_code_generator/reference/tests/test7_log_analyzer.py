import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_analyze_empty():
    assert LogAnalyzer().analyze([]) == {"total_requests": 0, "error_rate": 0.0}