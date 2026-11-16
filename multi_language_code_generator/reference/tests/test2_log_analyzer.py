import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_parse_404():
    line = '10.0.0.5 - - [10/Oct/2023:13:55:37 +0000] "GET /missing HTTP/1.1" 404 512'
    assert LogAnalyzer().parse_line(line)["status"] == 404