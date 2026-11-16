import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_parse_500_post():
    line = '10.0.0.6 - - [10/Oct/2023:13:55:38 +0000] "POST /api HTTP/1.1" 500 0'
    entry = LogAnalyzer().parse_line(line)
    assert entry["method"] == "POST" and entry["status"] == 500