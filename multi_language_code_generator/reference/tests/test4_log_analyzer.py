import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_parse_dash_bytes():
    line = '10.0.0.7 - - [10/Oct/2023:13:55:39 +0000] "GET /old HTTP/1.1" 301 -'
    assert LogAnalyzer().parse_line(line)["bytes"] == 0