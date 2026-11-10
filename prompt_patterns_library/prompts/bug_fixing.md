# Bug Fixing Prompt Template

**Role**: Act as an experienced software developer responsible for fixing bugs safely in an existing application.

**Task**: Investigate the reported bug, identify its cause from the supplied evidence, and propose the smallest reliable code change that restores the expected behavior. Preserve unrelated functionality and avoid speculative changes.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language and version
- `[BUG_DESCRIPTION]`: Description of the observed problem
- `[EXPECTED_BEHAVIOR]`: What should happen
- `[ACTUAL_BEHAVIOR]`: What currently happens
- `[CODE_BLOCK]`: Relevant source code
- `[REPRODUCTION_STEPS]`: Steps to reproduce the bug

**Expected Output**:
1. Root-cause explanation.
2. Minimal corrected code or a focused diff.
3. Explanation of why the fix works.
4. Regression test cases, including relevant edge cases.
5. Any assumptions or additional information needed.
