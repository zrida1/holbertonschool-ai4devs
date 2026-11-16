# Fix Validation Report

All four fixed files in `bug_fixes/` were executed in the same environment. Every result below comes from an actual run (exit code 0 = all assertions passed). Each fix was also checked against the original buggy logic as a negative control, to confirm the bug was real and the fix changes the outcome.

**Environment:** Python 3.13.18, Node.js v22.23.4, javac 21.0.12.1, g++ 13.3.0 (`-std=c++17 -Wall -Wextra`)

## bug1.py (Python)
- **Original Issue:** Off-by-one error in list slicing
- **Fix Applied:** Changed `items[-n + 1:]` to `items[-n:]`; added a guard `if n <= 0: return []`
- **Command:** `python3 bug1_fixed.py`
- **Test Results:** 6/6 assertions passed (exit code 0)
  - Last 3 elements: PASS
  - Last 1 element: PASS
  - n equals list length: PASS
  - n exceeds list length: PASS
  - n = 0 returns empty list: PASS
  - n = -2 returns empty list: PASS
- **Output:** `All Python tests passed.`
- **Negative control:** original `items[-3 + 1:]` on `[10, 20, 30, 40, 50]` returned `[40, 50]` instead of `[30, 40, 50]`

## bug2.js (JavaScript)
- **Original Issue:** Loop boundary `i <= prices.length` read one element past the end of the array
- **Fix Applied:** Changed `i <= prices.length` to `i < prices.length`; switched `console.assert` to Node's `assert.strictEqual`, because `console.assert` does not stop the process or change the exit code on failure
- **Command:** `node bug2_fixed.js`
- **Test Results:** 4/4 assertions passed (exit code 0)
  - Sum of `[10, 20, 30, 40]` = 100: PASS
  - Sum of `[5, 5]` = 10: PASS
  - Sum of single-element array `[15]` = 15: PASS
  - Sum of empty array = 0: PASS
- **Output:** `JavaScript tests passed.`
- **Negative control:** original loop on `[10, 20, 30, 40]` returned `NaN` instead of `100` (adds `undefined`)

## bug3.java (Java)
- **Original Issue:** Used `==` to compare `String` references instead of their contents
- **Fix Applied:** Replaced the reference comparison with `"admin".equals(username)`, which is also null-safe
- **Commands:** `javac bug3_fixed.java` then `java Bug3Fixed`
- **Test Results:** compiled without errors; 4/4 checks passed (exit code 0)
  - `new String("admin")` recognized as admin: PASS
  - `"user"` not recognized as admin: PASS
  - second `new String("admin")` recognized as admin: PASS
  - `null` does not throw and is not admin: PASS
- **Output:** `All Java tests passed.`
- **Negative control:** `new String("admin") == "admin"` evaluated to `false` (expected `true`)

## bug4.cpp (C++)
- **Original Issue:** Integer division truncated the average, and an empty vector led to division by zero
- **Fix Applied:** Cast the sum with `static_cast<double>(sum)` before dividing; added an early `return 0.0` for an empty vector
- **Commands:** `g++ -std=c++17 -Wall -Wextra -o bug4 bug4_fixed.cpp` then `./bug4`
- **Test Results:** compiled with no warnings; 4/4 assertions passed (exit code 0)
  - Average of `{10, 20, 25}` is within 18.33 to 18.34: PASS
  - Average of `{10, 20}` = 15.0: PASS
  - Average of `{5}` = 5.0: PASS
  - Average of `{}` = 0.0: PASS
- **Output:** `All C++ tests passed.`
- **Negative control:** integer division of 55 by 3 returned `18` instead of `18.33`

## Summary

| File | Language | Tests | Passed | Exit code |
|------|----------|-------|--------|-----------|
| bug1_fixed.py | Python | 6 | 6 | 0 |
| bug2_fixed.js | JavaScript | 4 | 4 | 0 |
| bug3_fixed.java | Java | 4 | 4 | 0 |
| bug4_fixed.cpp | C++ | 4 | 4 | 0 |
| **Total** | | **18** | **18** | |

**Result:** All four fixes are verified by actual execution. No failures.