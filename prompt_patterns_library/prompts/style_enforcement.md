# Style Enforcement Prompt Template

**Role**: Act as a software engineer and code-style specialist familiar with [LANGUAGE] conventions.

**Task**: Update the supplied code to follow the specified naming, formatting, and style rules. Preserve its logic and behavior. Do not make unrelated refactoring changes.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language
- `[CODE_BLOCK]`: Source code to format
- `[STYLE_GUIDELINES]`: Required naming, formatting, and coding rules
- `[FORMATTER_OR_LINTER]`: Required formatter or linter, if applicable

**Expected Output**:
1. The complete revised code in a code block.
2. A bullet list of style changes made.
3. Any guideline that could not be applied and why.
