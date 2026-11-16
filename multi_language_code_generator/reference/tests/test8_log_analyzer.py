import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402

OK = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326'
REDIRECT = '10.0.0.7 - - [10/Oct/2023:13:55:39 +0000] "GET /old HTTP/1.1" 301 -'


def test_analyze_no_errors():
    assert LogAnalyzer().analyze([OK, REDIRECT]) == {"total_requests": 2, "error_rate": 0.0}