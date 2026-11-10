# Test Coverage Analysis Prompt Template

**Role**: Act as a test quality analyst experienced in code coverage and test strategy.

**Task**: Analyze the supplied source code, existing tests, and coverage information. Identify important untested paths and recommend additional tests. Distinguish line, branch, and function coverage where the available data supports it.

**Input Placeholders**:
- `[SOURCE_CODE]`: Relevant application code
- `[EXISTING_TESTS]`: Current test suite
- `[COVERAGE_REPORT]`: Coverage report or metrics
- `[TEST_FRAMEWORK]`: Testing framework
- `[COVERAGE_GOALS]`: Project coverage targets, if any

**Expected Output**:
1. Summary of the available coverage evidence.
2. Untested or weakly tested areas with file or function references.
3. Recommended additional test scenarios.
4. Prioritized actions based on risk and importance.
5. Limitations caused by missing or incomplete coverage data.
