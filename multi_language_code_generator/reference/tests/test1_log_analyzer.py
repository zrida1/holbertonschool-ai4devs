import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402


def test_parse_ok_line():
    line = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326'
    assert LogAnalyzer().parse_line(line) == {
        "ip": "127.0.0.1", "method": "GET", "path": "/index.html",
        "status": 200, "bytes": 2326,
    }