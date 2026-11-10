# Unit Test Generation Prompt Template

**Role**: Act as a test engineer experienced in unit testing [LANGUAGE] applications.

**Task**: Generate focused unit tests for the supplied function, class, or component. Use the specified testing framework and test observable behavior rather than implementation details. Cover normal cases, boundary conditions, and expected failures.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language
- `[CODE_BLOCK]`: Code under test
- `[TEST_FRAMEWORK]`: Testing framework and version
- `[DEPENDENCIES_OR_MOCKS]`: Dependencies and mocking requirements
- `[EXPECTED_BEHAVIOR]`: Relevant behavior and business rules

**Expected Output**:
1. Complete test code in a code block.
2. Test names and a brief description of each scenario.
3. Explanation of mocks, stubs, or fixtures used.
4. Any uncovered cases or assumptions.
