import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402

NOT_FOUND = '10.0.0.5 - - [10/Oct/2023:13:55:37 +0000] "GET /missing HTTP/1.1" 404 512'
SERVER_ERR = '10.0.0.6 - - [10/Oct/2023:13:55:38 +0000] "POST /api HTTP/1.1" 500 0'


def test_analyze_all_errors():
    assert LogAnalyzer().analyze([NOT_FOUND, SERVER_ERR]) == {"total_requests": 2, "error_rate": 100.0}