# Bug Reports – AI-Assisted Debugging

This document contains structured reports for the five bugs identified and fixed during the AI-assisted debugging process.

## Bug Report – bug1.py

- **File Name:** `bug1.py`
- **Bug Summary:** The Python program could not run because of a syntax error in the `if` statement inside the `calculate_discount()` function.
- **Root Cause:** A colon (`:`) was missing after the condition `if customer_type == "student"`. Python requires a colon at the end of conditional statements.
- **Resolution:**
  - **AI-generated suggestion:** Add the missing colon after the `if` condition.
  - **Manual fix:** Updated the statement to `if customer_type == "student":` and checked that the discount calculation remained unchanged.
- **Lessons Learned:** Small syntax mistakes can prevent an entire program from running. Always check conditional statement syntax and test the program after making changes.

## Bug Report – bug2.py

- **File Name:** `bug2.py`
- **Bug Summary:** The `get_average()` function caused a runtime error when it received an empty list.
- **Root Cause:** The function divided the sum of the numbers by the length of the list without checking whether the list was empty. Dividing by zero raises a `ZeroDivisionError`.
- **Resolution:**
  - **AI-generated suggestion:** Check whether the input list is empty before performing the division.
  - **Manual fix:** Added an empty-list check that raises a `ValueError` with a clear error message.
- **Lessons Learned:** Functions should handle edge cases, not only normal inputs. Always test empty collections and invalid inputs to prevent unexpected runtime errors.

## Bug Report – bug3.js

- **File Name:** `bug3.js`
- **Bug Summary:** The `getFirstUsers()` function returned one more user than requested.
- **Root Cause:** The `for` loop used `i <= count` instead of `i < count`. Since array indexes start at zero, the loop executed one extra time.
- **Resolution:**
  - **AI-generated suggestion:** Replace the `<=` operator with `<` in the loop condition.
  - **Manual fix:** Updated the loop condition to `i < count && i < users.length`. The additional array-length check prevents accessing indexes outside the array.
- **Lessons Learned:** Off-by-one errors are common in loops. Test boundary values such as zero, one, and values greater than the array length.

## Bug Report – bug4.js

- **File Name:** `bug4.js`
- **Bug Summary:** The shopping cart total calculation produced incorrect results and caused an error when formatting the final total.
- **Root Cause:** The `calculateCartTotal()` function used `toFixed(2)`, which converts a number into a string. The `applyTax()` function then used the `+` operator with this string, causing string concatenation instead of numeric addition.
- **Resolution:**
  - **AI-generated suggestion:** Keep the calculation result as a number and use `toFixed(2)` only when displaying the result.
  - **Manual fix:** Removed `toFixed(2)` from the return statement of `calculateCartTotal()`. Formatting was moved to the output statements in `main()`.
- **Lessons Learned:** JavaScript distinguishes between numbers and strings. Always check data types when performing calculations, and format numeric values only when displaying them.

## Bug Report – bug5.java

- **File Name:** `bug5.java`
- **Bug Summary:** The `containsUser()` method did not reliably find a user name when comparing Java strings.
- **Root Cause:** The code used `==` to compare strings. In Java, `==` compares object references rather than the actual string contents.
- **Resolution:**
  - **AI-generated suggestion:** Replace `==` with the `.equals()` method to compare string values.
  - **Manual fix:** Updated the condition to `user.equals(target)`, ensuring that the actual contents of the strings are compared.
- **Lessons Learned:** In Java, `==` and `.equals()` have different purposes. Use `.equals()` for comparing string contents and test with separate String objects containing the same text.

---

## Overall Conclusion

The debugging process covered five different types of programming errors: syntax, runtime, off-by-one, data type, and logical errors.

AI assistance helped identify the root causes and suggest possible solutions. Manual review was also important for checking the suggestions, making small improvements, and ensuring that the fixes matched the intended behavior.

This task demonstrated that AI can support debugging, but developers should still understand, review, and validate every suggested change.