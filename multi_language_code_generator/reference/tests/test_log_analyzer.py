import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from log_analyzer import LogAnalyzer  # noqa: E402

OK = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326'
NOT_FOUND = '10.0.0.5 - - [10/Oct/2023:13:55:37 +0000] "GET /missing HTTP/1.1" 404 512'
SERVER_ERR = '10.0.0.6 - - [10/Oct/2023:13:55:38 +0000] "POST /api HTTP/1.1" 500 0'
REDIRECT = '10.0.0.7 - - [10/Oct/2023:13:55:39 +0000] "GET /old HTTP/1.1" 301 -'


@pytest.fixture
def analyzer():
    return LogAnalyzer()


def test_parse_ok_line(analyzer):
    assert analyzer.parse_line(OK) == {
        "ip": "127.0.0.1", "method": "GET", "path": "/index.html",
        "status": 200, "bytes": 2326,
    }


def test_parse_404(analyzer):
    assert analyzer.parse_line(NOT_FOUND)["status"] == 404


def test_parse_500_post(analyzer):
    entry = analyzer.parse_line(SERVER_ERR)
    assert entry["method"] == "POST" and entry["status"] == 500


def test_parse_dash_bytes(analyzer):
    assert analyzer.parse_line(REDIRECT)["bytes"] == 0


def test_parse_malformed_raises(analyzer):
    with pytest.raises(ValueError):
        analyzer.parse_line("this is not a log line")


def test_parse_empty_raises(analyzer):
    with pytest.raises(ValueError):
        analyzer.parse_line("")


def test_analyze_empty(analyzer):
    assert analyzer.analyze([]) == {"total_requests": 0, "error_rate": 0.0}


def test_analyze_no_errors(analyzer):
    assert analyzer.analyze([OK, REDIRECT]) == {"total_requests": 2, "error_rate": 0.0}


def test_analyze_all_errors(analyzer):
    assert analyzer.analyze([NOT_FOUND, SERVER_ERR]) == {"total_requests": 2, "error_rate": 100.0}


def test_analyze_mixed(analyzer):
    result = analyzer.analyze([OK, OK, OK, NOT_FOUND])
    assert result == {"total_requests": 4, "error_rate": 25.0}


def test_analyze_rounding(analyzer):
    result = analyzer.analyze([OK, OK, NOT_FOUND])
    assert result["error_rate"] == 33.33


def test_analyze_skips_malformed(analyzer):
    result = analyzer.analyze([OK, "garbage", NOT_FOUND])
    assert result == {"total_requests": 2, "error_rate": 50.0}