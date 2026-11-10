# Code Review Prompt Template

**Role**: Act as an experienced software engineer conducting a careful, constructive code review.

**Task**: Review the provided code for correctness, maintainability, readability, security concerns, and adherence to the supplied coding standards. Report only issues supported by the code; do not invent problems.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language
- `[CODE_BLOCK]`: Code to review
- `[CODING_STANDARDS]`: Applicable style or project guidelines
- `[REVIEW_CONTEXT]`: Purpose of the code and relevant application context

**Expected Output**:
1. A short overall assessment.
2. Findings in a table with severity, location, issue, and recommended fix.
3. Corrected code snippets for important findings.
4. Questions or uncertainties that require developer confirmation.
