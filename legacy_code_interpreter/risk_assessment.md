# Risk Assessment – COBOL Book Sample

## 1. Overview

This document identifies potential risks in the COBOL Book Sample application.

The assessment focuses on file handling, command-line argument processing, data validation, error handling, and communication between COBOL programs.

Risks are prioritized according to their potential impact on application reliability, maintainability, and data integrity.

## 2. Risk Assessment Table

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| Hardcoded File Configuration | High | The `-f` command-line option does not properly affect the file used by the application. The execution section uses a fixed filename (`books.dat`). This may cause users to access an unexpected file. |
| Insufficient Error Handling | High | File operations rely heavily on status codes. Unexpected errors may not be clearly distinguished from normal conditions, making failures difficult to diagnose. |
| Missing Input Validation | High | Book information and command-line arguments do not have sufficient validation in some processing sections. Invalid input may cause unexpected behavior or incorrect records. |
| Data Integrity Issues | High | Errors during indexed file operations or incomplete validation may result in incorrect or inconsistent book records. |
| Tight Coupling Between Programs | Medium | The CLI and BookLegacy programs depend on shared data structures and operation codes. Changes to shared declarations may affect multiple components. |
| Complex Command-Line Processing | Medium | Command and option processing uses multiple conditions and state variables. Missing option values and invalid combinations may not be handled clearly. |
| Mixed Responsibilities | Medium | File operations, business logic, and error handling are closely connected, making individual components harder to test and maintain. |
| Use of Hardcoded Status and Operation Codes | Low | Values such as `"00"`, `"23"`, and single-character operation codes are used directly. This reduces readability and makes future changes more difficult. |

## 3. Risk Prioritization

### High Severity

**1. Hardcoded File Configuration**

The application may ignore the filename supplied by the user. This can lead to unexpected file access and operational errors.

**Recommended action:** Correct the filename configuration and add tests for custom file paths.

**2. Insufficient Error Handling**

Unexpected file errors may be treated similarly to normal end-of-file conditions.

**Recommended action:** Handle normal completion and unexpected file errors separately. Provide meaningful error messages.

**3. Missing Input Validation**

Invalid user input may reach the business logic without sufficient checks.

**Recommended action:** Validate command-line arguments and book fields before processing.

**4. Data Integrity Issues**

Incorrect or incomplete file operations can affect stored book information.

**Recommended action:** Add validation, duplicate-record checks, and tests for file operation failures.

### Medium Severity

**5. Tight Coupling Between Programs**

Shared structures make changes more difficult because multiple programs depend on the same declarations.

**Recommended action:** Centralize shared declarations and document program interfaces.

**6. Complex Command-Line Processing**

The current argument-processing logic can be difficult to understand and extend.

**Recommended action:** Separate argument parsing from command execution and validate each option independently.

**7. Mixed Responsibilities**

Combining file access and business logic increases maintenance complexity.

**Recommended action:** Separate file operations, business rules, and presentation logic.

### Low Severity

**8. Hardcoded Status and Operation Codes**

Directly using numeric and character values makes the code less readable.

**Recommended action:** Define named constants or centralized declarations in a shared copybook.

## 4. Overall Risk Summary

| Severity | Number of Risks |
| :--- | :---: |
| High | 4 |
| Medium | 3 |
| Low | 1 |
| **Total** | **8** |

## 5. Conclusion

The main risks in the COBOL Book Sample application are related to file configuration, error handling, input validation, and data integrity.

High-severity risks should be addressed first because they can affect application correctness and reliability.

A gradual modernization strategy is recommended. The first steps should include fixing configuration handling, improving validation, introducing automated tests, and separating responsibilities between program components.

These improvements can reduce technical debt while preserving the application's existing functionality.