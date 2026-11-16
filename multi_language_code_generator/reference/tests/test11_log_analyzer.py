import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402

OK = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326'
NOT_FOUND = '10.0.0.5 - - [10/Oct/2023:13:55:37 +0000] "GET /missing HTTP/1.1" 404 512'


def test_analyze_rounding():
    assert LogAnalyzer().analyze([OK, OK, NOT_FOUND])["error_rate"] == 33.33