# Cross-Language Specification - Log Analyzer

## 1. Algorithm Description

The Log Analyzer processes web server log entries and generates statistics about HTTP requests.

The algorithm analyzes log entries to calculate:

- Total number of valid requests.
- Number of unique visitors based on IP addresses.
- Number of successful requests.
- Number of failed requests (HTTP status codes 400–599).
- Error rate as a percentage.
- Distribution of HTTP status codes.
- Most frequently requested endpoints.

The algorithm must produce equivalent results regardless of the programming language used for its implementation.

## 2. Input Format

The algorithm accepts a list of log entries as strings.

Each valid log entry must follow this format:

`IP_ADDRESS HTTP_METHOD ENDPOINT STATUS_CODE`

Example:

```text
192.168.1.10 GET /home 200
192.168.1.11 POST /login 201
192.168.1.10 GET /products 404
192.168.1.12 GET /home 500
```

### Input Requirements

- Each entry must contain exactly four fields separated by whitespace.
- IP address must be a non-empty string without whitespace.
- HTTP method must contain uppercase letters only.
- Endpoint must start with `/`.
- HTTP status code must be an integer between 100 and 599.
- Invalid entries must be ignored when calculating request statistics.

## 3. Output Format

The algorithm returns a JSON object containing the calculated statistics.

Example:

```json
{
  "total_requests": 4,
  "unique_visitors": 3,
  "successful_requests": 2,
  "failed_requests": 2,
  "error_rate": 50.0,
  "status_codes": {
    "200": 1,
    "201": 1,
    "404": 1,
    "500": 1
  },
  "top_endpoints": [
    {
      "endpoint": "/home",
      "count": 2
    },
    {
      "endpoint": "/login",
      "count": 1
    },
    {
      "endpoint": "/products",
      "count": 1
    }
  ]
}
```

### Output Requirements

- `total_requests`: Number of valid log entries.
- `unique_visitors`: Number of distinct IP addresses.
- `successful_requests`: Number of requests with status codes between 100 and 399.
- `failed_requests`: Number of requests with status codes between 400 and 599.
- `error_rate`: Percentage of failed requests, rounded to two decimal places.
- `status_codes`: Number of occurrences of each HTTP status code.
- `top_endpoints`: Endpoints sorted by request count in descending order.

If two endpoints have the same request count, they must be sorted alphabetically by endpoint.

If there are no valid requests, `error_rate` must be `0.0`, and all other statistics must contain zero values or empty collections.

## 4. Edge Cases

The implementation must correctly handle the following situations:

1. Empty input list.
2. Input containing only malformed log entries.
3. Multiple requests from the same IP address.
4. Requests with different HTTP status codes.
5. Requests with invalid status codes.
6. Log entries with missing or extra fields.
7. Multiple endpoints with the same request count.
8. A log containing only failed requests.
9. A log containing only successful requests.

## 5. Test Cases

### Test Case 1 - Normal Log Entries

**Input:**

```text
192.168.1.10 GET /home 200
192.168.1.11 POST /login 201
192.168.1.10 GET /products 404
192.168.1.12 GET /home 500
```

**Expected Output:**

- Total requests: 4
- Unique visitors: 3
- Successful requests: 2
- Failed requests: 2
- Error rate: 50.0%
- Status codes: 200 (1), 201 (1), 404 (1), 500 (1)
- Top endpoints: /home (2), /login (1), /products (1)

### Test Case 2 - Empty Input

**Input:**

```text
[]
```

**Expected Output:**

- Total requests: 0
- Unique visitors: 0
- Successful requests: 0
- Failed requests: 0
- Error rate: 0.0%
- Status codes: {}
- Top endpoints: []

### Test Case 3 - Duplicate Visitors

**Input:**

```text
10.0.0.1 GET /home 200
10.0.0.1 GET /about 200
10.0.0.1 POST /login 201
10.0.0.2 GET /home 200
```

**Expected Output:**

- Total requests: 4
- Unique visitors: 2
- Successful requests: 4
- Failed requests: 0
- Error rate: 0.0%
- Status codes: 200 (3), 201 (1)
- Top endpoints: /home (2), /about (1), /login (1)

### Test Case 4 - Invalid Log Entries

**Input:**

```text
192.168.1.10 GET /home 200
invalid log entry
192.168.1.11 POST /login abc
192.168.1.12 GET home 404
192.168.1.13 GET /about 600
192.168.1.14 GET /products 404
```

**Expected Output:**

- Total requests: 2
- Unique visitors: 2
- Successful requests: 1
- Failed requests: 1
- Error rate: 50.0%
- Status codes: 200 (1), 404 (1)
- Top endpoints: /home (1), /products (1)

### Test Case 5 - Only Failed Requests

**Input:**

```text
192.168.1.10 GET /home 404
192.168.1.11 POST /login 500
192.168.1.12 GET /products 403
```

**Expected Output:**

- Total requests: 3
- Unique visitors: 3
- Successful requests: 0
- Failed requests: 3
- Error rate: 100.0%
- Status codes: 403 (1), 404 (1), 500 (1)
- Top endpoints: /home (1), /login (1), /products (1)

### Test Case 6 - Equal Endpoint Frequencies

**Input:**

```text
192.168.1.10 GET /products 200
192.168.1.11 GET /home 200
192.168.1.12 GET /about 200
192.168.1.13 GET /home 200
192.168.1.14 GET /products 200
```

**Expected Output:**

- Total requests: 5
- Unique visitors: 5
- Successful requests: 5
- Failed requests: 0
- Error rate: 0.0%
- Status codes: 200 (5)
- Top endpoints: /home (2), /products (2), /about (1)

## 6. Cross-Language Requirements

The algorithm will be implemented in at least three programming languages:

- Python
- Java
- JavaScript (Node.js)

All implementations must:

- Follow this specification.
- Produce equivalent results for the same input.
- Handle all defined edge cases.
- Pass the same set of test cases.
- Follow the conventions and idioms of the respective programming language.

## 7. Validation and Performance

Functional equivalence will be validated by running the same test cases against all implementations.

Performance will be evaluated using the same input dataset and comparable execution conditions.

The benchmark will measure:

- Execution time.
- Correctness of output.
- Memory usage, where practical.

All differences in implementation approaches, language-specific features, and performance will be documented.

## 8. Assumptions

- Each input string represents one log entry.
- IP addresses are treated as identifiers and are not validated against real IPv4 or IPv6 formats.
- HTTP methods must contain uppercase letters only.
- Only valid entries contribute to the statistics.
- Error rate is calculated as `(failed_requests / total_requests) * 100`.
- Error rate is rounded to two decimal places.
- Endpoint sorting uses request count first and alphabetical order second.