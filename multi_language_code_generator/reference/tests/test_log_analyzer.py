
import unittest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()

    # Test 1: Normal log entries
    def test_normal_entries(self):
        logs = [
            "192.168.1.10 GET /home 200",
            "192.168.1.11 POST /login 201",
            "192.168.1.10 GET /products 404",
            "192.168.1.12 GET /home 500"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["unique_visitors"], 3)
        self.assertEqual(result["successful_requests"], 2)
        self.assertEqual(result["failed_requests"], 2)
        self.assertEqual(result["error_rate"], 50.0)

    # Test 2: Empty input
    def test_empty_input(self):
        result = self.analyzer.analyze([])

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["successful_requests"], 0)
        self.assertEqual(result["failed_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["status_codes"], {})
        self.assertEqual(result["top_endpoints"], [])

    # Test 3: Duplicate visitors
    def test_duplicate_visitors(self):
        logs = [
            "10.0.0.1 GET /home 200",
            "10.0.0.1 GET /about 200",
            "10.0.0.1 POST /login 201",
            "10.0.0.2 GET /home 200"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["total_requests"], 4)

    # Test 4: Invalid log entries are ignored
    def test_invalid_entries(self):
        logs = [
            "192.168.1.10 GET /home 200",
            "invalid log entry",
            "192.168.1.11 POST /login abc",
            "192.168.1.12 GET home 404",
            "192.168.1.13 GET /about 600",
            "192.168.1.14 GET /products 404"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["failed_requests"], 1)
        self.assertEqual(result["error_rate"], 50.0)

    # Test 5: Only failed requests
    def test_only_failed_requests(self):
        logs = [
            "192.168.1.10 GET /home 404",
            "192.168.1.11 POST /login 500",
            "192.168.1.12 GET /products 403"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["successful_requests"], 0)
        self.assertEqual(result["failed_requests"], 3)
        self.assertEqual(result["error_rate"], 100.0)

    # Test 6: Only successful requests
    def test_only_successful_requests(self):
        logs = [
            "192.168.1.10 GET /home 200",
            "192.168.1.11 POST /login 201",
            "192.168.1.12 GET /about 302"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["successful_requests"], 3)
        self.assertEqual(result["failed_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    # Test 7: Equal endpoint frequencies
    def test_equal_endpoint_frequencies(self):
        logs = [
            "192.168.1.10 GET /products 200",
            "192.168.1.11 GET /home 200",
            "192.168.1.12 GET /about 200",
            "192.168.1.13 GET /home 200",
            "192.168.1.14 GET /products 200"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(
            result["top_endpoints"],
            [
                {"endpoint": "/home", "count": 2},
                {"endpoint": "/products", "count": 2},
                {"endpoint": "/about", "count": 1}
            ]
        )

    # Test 8: Invalid status code boundaries
    def test_invalid_status_codes(self):
        logs = [
            "192.168.1.10 GET /home 99",
            "192.168.1.11 GET /home 600",
            "192.168.1.12 GET /home 200"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 1)

    # Test 9: HTTP status code boundaries
    def test_status_code_boundaries(self):
        logs = [
            "192.168.1.10 GET /a 100",
            "192.168.1.11 GET /b 399",
            "192.168.1.12 GET /c 400",
            "192.168.1.13 GET /d 599"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["successful_requests"], 2)
        self.assertEqual(result["failed_requests"], 2)
        self.assertEqual(result["error_rate"], 50.0)

    # Test 10: Malformed entries only
    def test_only_malformed_entries(self):
        logs = [
            "invalid",
            "",
            "192.168.1.10 GET",
            "192.168.1.11 GET /home abc"
        ]

        result = self.analyzer.analyze(logs)

        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    # Test 11: Parse a valid log entry
    def test_parse_valid_entry(self):
        result = self.analyzer.parse_line(
            "192.168.1.10 GET /home 200"
        )

        self.assertEqual(result["ip"], "192.168.1.10")
        self.assertEqual(result["method"], "GET")
        self.assertEqual(result["endpoint"], "/home")
        self.assertEqual(result["status"], 200)

    # Test 12: Parse an invalid log entry
    def test_parse_invalid_entry(self):
        result = self.analyzer.parse_line(
            "192.168.1.10 get home abc"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
