# Fix Validation Report

This document describes the fixes applied to the four buggy code snippets and the test cases prepared to verify their correctness.

## 1. bug1.py – Python

- **Original Issue:** Off-by-one error in list slicing.
- **Fix Applied:** Changed `items[-n + 1:]` to `items[-n:]`.
- **Additional Handling:** Preserved behavior for zero and negative values of `n`.
- **Test Cases:**
  - Return the last 3 elements.
  - Return the last 1 element.
  - Return all elements when `n` equals the list length.
  - Return all elements when `n` exceeds the list length.
  - Return an empty list when `n` is zero or negative.
- **Validation:** Six assertion-based test cases included in `bug1_fixed.py`.
- **Expected Result:** All six test cases should pass.

## 2. bug2.js – JavaScript

- **Original Issue:** Incorrect loop boundary caused an out-of-bounds array access.
- **Fix Applied:** Changed the loop condition from `i <= prices.length` to `i < prices.length`.
- **Test Cases:**
  - Calculate the total of `[10, 20, 30, 40]`.
  - Calculate the total of `[5, 5]`.
  - Calculate the total of a single-element array.
  - Calculate the total of an empty array.
- **Validation:** Four test cases included in `bug2_fixed.js`.
- **Expected Result:** All test cases should return the correct sum without producing `NaN`.

## 3. bug3.java – Java

- **Original Issue:** Used `==` to compare String references instead of their contents.
- **Fix Applied:** Replaced the reference comparison with `"admin".equals(username)`.
- **Additional Handling:** The constant String is used on the left side to safely handle null values.
- **Test Cases:**
  - Recognize a new String object containing `"admin"`.
  - Reject a regular username.
  - Recognize another String object with the same content.
  - Safely handle a null username.
- **Validation:** Four assertion-based test cases included in `bug3_fixed.java`.
- **Expected Result:** All four test cases should pass.

## 4. bug4.cpp – C++

- **Original Issue:** Integer division removed the fractional part of the average.
- **Fix Applied:** Converted `sum` to `double` using `static_cast<double>(sum)` before division.
- **Additional Handling:** Preserved the empty-vector check.
- **Test Cases:**
  - Calculate the average of `{10, 20, 25}`.
  - Calculate the average of `{10, 20}`.
  - Calculate the average of a single-element vector.
  - Calculate the average of an empty vector.
- **Validation:** Four assertion-based test cases included in `bug4_fixed.cpp`.
- **Expected Result:** All four test cases should pass, including the decimal result of approximately 18.33.

## Overall Summary

| File | Fix | Test Cases |
|---|---|---:|
| bug1_fixed.py | Corrected list slicing | 6 |
| bug2_fixed.js | Corrected loop boundary | 4 |
| bug3_fixed.java | Corrected String comparison | 4 |
| bug4_fixed.cpp | Corrected integer division | 4 |
| **Total** | **4 bugs addressed** | **18** |

## Conclusion

All four identified bugs have corresponding fixes and test cases. The tests cover the original issues as well as important edge cases.

The fixes are prepared for validation in their respective programming environments. Actual test execution results should be recorded after running the commands below.