
from collections import Counter
import re


class LogAnalyzer:

    def parse_line(self, line: str) -> dict | None:
        """Parse one log entry. Return None if the entry is invalid."""

        fields = line.split()

        if len(fields) != 4:
            return None

        ip_address, method, endpoint, status_text = fields

        # Validate HTTP method
        if not re.fullmatch(r"[A-Z]+", method):
            return None

        # Validate endpoint
        if not endpoint.startswith("/"):
            return None

        # Validate status code
        if not status_text.isdigit():
            return None

        status_code = int(status_text)

        if not 100 <= status_code <= 599:
            return None

        return {
            "ip": ip_address,
            "method": method,
            "endpoint": endpoint,
            "status": status_code
        }

    def analyze(self, lines: list[str]) -> dict:
        """Analyze log entries and return request statistics."""

        valid_entries = []

        for line in lines:
            entry = self.parse_line(line)

            if entry is not None:
                valid_entries.append(entry)

        total_requests = len(valid_entries)

        unique_visitors = len({
            entry["ip"] for entry in valid_entries
        })

        successful_requests = sum(
            1 for entry in valid_entries
            if 100 <= entry["status"] <= 399
        )

        failed_requests = sum(
            1 for entry in valid_entries
            if 400 <= entry["status"] <= 599
        )

        error_rate = (
            round((failed_requests / total_requests) * 100, 2)
            if total_requests > 0 else 0.0
        )

        status_counts = Counter(
            entry["status"] for entry in valid_entries
        )

        status_codes = {
            str(code): status_counts[code]
            for code in sorted(status_counts)
        }

        endpoint_counts = Counter(
            entry["endpoint"] for entry in valid_entries
        )

        top_endpoints = [
            {
                "endpoint": endpoint,
                "count": count
            }
            for endpoint, count in sorted(
                endpoint_counts.items(),
                key=lambda item: (-item[1], item[0])
            )
        ]

        return {
            "total_requests": total_requests,
            "unique_visitors": unique_visitors,
            "successful_requests": successful_requests,
            "failed_requests": failed_requests,
            "error_rate": error_rate,
            "status_codes": status_codes,
            "top_endpoints": top_endpoints
        }
