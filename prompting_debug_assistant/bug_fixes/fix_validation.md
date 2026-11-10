# Fix Validation Report

This document records the corrected code snippets, test cases, expected results, and actual results. Each fix was validated using normal inputs and relevant edge cases.

## Bug 1 – `bug1_fixed.py`

**Issue**: Missing colon in the `if` statement (Syntax Error).

**Fix Applied**: Added the missing colon after the student customer condition.

**Test Cases**:

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| Price = 100, Type = student | 90.0 | 90.0 | PASS |
| Price = 100, Type = member | 85.0 | 85.0 | PASS |
| Price = 100, Type = regular | 100.0 | 100.0 | PASS |
| Price = -10, Type = student | ValueError | ValueError | PASS |

**Validation**: The program runs without syntax errors and calculates discounts correctly.

**Manual Tweaks**: None.

---

## Bug 2 – `bug2_fixed.py`

**Issue**: Division by zero when calculating the average of an empty list.

**Fix Applied**: Added an empty-list check and raised a descriptive `ValueError`.

**Test Cases**:

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| [88, 92, 79] | 86.33 | 86.33 | PASS |
| [100, 90] | 95.0 | 95.0 | PASS |
| [] | ValueError | ValueError | PASS |

**Validation**: The function calculates averages correctly and handles empty input safely.

**Manual Tweaks**: None.

---

## Bug 3 – `bug3_fixed.js`

**Issue**: Off-by-one error caused by using `i <= count`.

**Fix Applied**: Changed the loop condition to `i < count` and added an array-length check.

**Test Cases**:

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| count = 2 | ["Amina", "Murad"] | ["Amina", "Murad"] | PASS |
| count = 0 | [] | [] | PASS |
| count = 10 | All 4 users | All 4 users | PASS |

**Validation**: The function returns the requested number of users without exceeding the array length.

**Manual Tweaks**: Added the array-length condition to prevent unnecessary iterations.

---

## Bug 4 – `bug4_fixed.js`

**Issue**: `toFixed()` returned a string, causing incorrect type handling during tax calculation.

**Fix Applied**: Kept the subtotal as a number and moved formatting to the output stage.

**Test Cases**:

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| Cart subtotal | 28.75 | 28.75 | PASS |
| Tax rate = 0.08 | 31.05 | 31.05 | PASS |
| Subtotal data type | number | number | PASS |
| Final total data type | number | number | PASS |

**Validation**: The subtotal and final total remain numeric during calculations. Formatting is applied only when displaying the results.

**Manual Tweaks**: Moved `toFixed(2)` from the calculation function to the console output.

---

## Bug 5 – `bug5_fixed.java`

**Issue**: Used `==` to compare Java String references instead of their contents.

**Fix Applied**: Replaced `user == target` with `user.equals(target)`.

**Test Cases**:

| Input | Expected Output | Actual Output | Result |
|---|---|---|---|
| Search "Murad" | true | true | PASS |
| Search "Rashad" | false | false | PASS |
| Search "Amina" | true | true | PASS |

**Validation**: The Java class compiles and correctly compares string contents, even when strings are separate objects.

**Manual Tweaks**: None.

---

## Overall Validation Summary

| Bug | Language | Main Issue | Status |
|---|---|---|---|
| Bug 1 | Python | Syntax Error | PASS |
| Bug 2 | Python | Runtime Exception | PASS |
| Bug 3 | JavaScript | Off-by-one Error | PASS |
| Bug 4 | JavaScript | Data Type Error | PASS |
| Bug 5 | Java | String Comparison | PASS |

**Conclusion**:

All five buggy snippets have been corrected. The selected fixes address the identified issues and pass the documented test cases. Edge cases were also included to verify that the corrected code behaves as expected.

No additional manual changes were required beyond the documented fixes and the array-length safeguard in Bug 3.
