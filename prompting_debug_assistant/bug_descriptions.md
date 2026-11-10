# Bug Descriptions

This document describes the intended behavior of each deliberately flawed code snippet. The snippets are prepared for the AI-assisted debugging tasks. They should be analyzed and tested before any fixes are applied.

## Bug 1 – `bug1.py`

**Intended Behavior**: Calculate and return the final product price after applying a discount based on the customer's type. Students receive a 10% discount, members receive a 15% discount, and other customers receive no discount. Negative prices should be rejected.

**Issue Type**: Syntax error.

**Notes**: The program should run and print the final price for a student customer. Inspect the conditional statement in the discount calculation.

## Bug 2 – `bug2.py`

**Intended Behavior**: Calculate and print the average score of all students in a class. The function should handle the input safely, including the case where there are no student scores.

**Issue Type**: Runtime exception / missing edge-case handling.

**Notes**: The provided example contains student scores, but the average function may fail when it receives an empty collection. Test both non-empty and empty inputs.

## Bug 3 – `bug3.js`

**Intended Behavior**: Return the names of the first `count` users from the supplied array. If `count` is greater than the number of available users, return all available user names.

**Issue Type**: Off-by-one / loop logic error.

**Notes**: When `count` is 2, the function should return exactly two names. Also test values of 0, 1, and a value greater than the array length.

## Bug 4 – `bug4.js`

**Intended Behavior**: Calculate the shopping cart subtotal and then add tax using the supplied tax rate. Both values should be numeric so that the final total can be calculated and formatted to two decimal places.

**Issue Type**: Data type / number handling error.

**Notes**: Test the calculation with the provided cart. Pay attention to the type returned by the subtotal calculation and how it is used in the tax calculation.

## Bug 5 – `UserSearch.java`

**Intended Behavior**: Search an array of user names and return `true` if an entry has the same text as the target name, regardless of whether the strings are separate objects. Otherwise, return `false`.

**Issue Type**: Logical error / misuse of string comparison.

**Notes**: The example creates the search name as a separate `String` object. The search should still find the matching text in the array.
