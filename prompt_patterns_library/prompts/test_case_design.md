# Test Case Design Prompt Template

**Role**: Act as a QA engineer experienced in functional testing and test design techniques.

**Task**: Convert the supplied feature requirements into clear, testable cases. Include positive, negative, boundary, and relevant alternative scenarios. Avoid duplicating cases and identify ambiguous requirements.

**Input Placeholders**:
- `[FEATURE_DESCRIPTION]`: Feature or requirement description
- `[ACCEPTANCE_CRITERIA]`: Conditions for acceptance
- `[USER_ROLES]`: Relevant user types and permissions
- `[TEST_ENVIRONMENT]`: Environment or platform
- `[CONSTRAINTS]`: Known limitations or dependencies

**Expected Output**:
A table containing:
- Test case ID
- Scenario and objective
- Preconditions
- Test steps
- Test data
- Expected result
- Priority

Also include a short list of ambiguities or missing requirements.
