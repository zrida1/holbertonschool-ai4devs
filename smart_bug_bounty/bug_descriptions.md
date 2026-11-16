# Bug Descriptions

This document describes the intended behavior and known issues of the buggy code snippets prepared for the Smart Bug Bounty project.

## bug1.py – Python

- **Language:** Python
- **Intended Behavior:** Return the last `n` items from a given list. If `n` is greater than the list length, return the entire list. If `n` is zero or negative, return an empty list.
- **Current Issue:** The slicing expression uses `-n + 1`, which causes the function to return one fewer item than requested.
- **Bug Type:** Off-by-one error.
- **Expected Fix:** Correct the list slicing expression.

## bug2.js – JavaScript

- **Language:** JavaScript
- **Intended Behavior:** Calculate and return the sum of all numbers in an array.
- **Current Issue:** The loop condition uses `i <= prices.length`, causing the loop to access an array index that does not exist. This results in `NaN`.
- **Bug Type:** Boundary condition error.
- **Expected Fix:** Correct the loop condition to prevent accessing an invalid array index.

## bug3.java – Java

- **Language:** Java
- **Intended Behavior:** Check whether a given username matches the administrator username `"admin"`.
- **Current Issue:** The method uses the `==` operator to compare String objects. This compares object references instead of their actual text values.
- **Bug Type:** Incorrect String comparison.
- **Expected Fix:** Use an appropriate String content comparison method.

## bug4.cpp – C++

- **Language:** C++
- **Intended Behavior:** Calculate and return the arithmetic average of all numbers in a vector as a decimal value. Return zero if the vector is empty.
- **Current Issue:** The division is performed using integer operands, which removes the fractional part of the result.
- **Bug Type:** Integer division error.
- **Expected Fix:** Convert one operand to a floating-point type before performing the division.