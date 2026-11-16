"""Reference implementation of LogAnalyzer (Python baseline).

Parses Apache Common/Combined log lines and computes simple statistics.
This is the specification other language ports must match exactly.

Spec
----
parse_line(line) -> dict
    Input : one Apache log line, e.g.
            127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
    Output: {"ip": str, "method": str, "path": str, "status": int, "bytes": int}
    Error : raises ValueError if the line is malformed.
    Note  : bytes is 0 when the log contains "-".

analyze(lines) -> dict
    Output: {"total_requests": int, "error_rate": float}
    error_rate = percentage (0-100) of requests with status >= 400,
    rounded to 2 decimals. Empty input -> total 0, error_rate 0.0.
    Malformed lines are skipped and not counted.
"""

import re

_LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[[^\]]+\] '
    r'"(?P<method>[A-Z]+) (?P<path>\S+)[^"]*" '
    r'(?P<status>\d{3}) (?P<bytes>\d+|-)'
)


class LogAnalyzer:
    def parse_line(self, line: str) -> dict:
        match = _LOG_PATTERN.match(line.strip())
        if not match:
            raise ValueError(f"Malformed log line: {line!r}")
        size = match.group("bytes")
        return {
            "ip": match.group("ip"),
            "method": match.group("method"),
            "path": match.group("path"),
            "status": int(match.group("status")),
            "bytes": 0 if size == "-" else int(size),
        }

    def analyze(self, lines: list) -> dict:
        total = 0
        errors = 0
        for line in lines:
            try:
                entry = self.parse_line(line)
            except ValueError:
                continue
            total += 1
            if entry["status"] >= 400:
                errors += 1
        error_rate = round(errors / total * 100, 2) if total else 0.0
        return {"total_requests": total, "error_rate": error_rate}