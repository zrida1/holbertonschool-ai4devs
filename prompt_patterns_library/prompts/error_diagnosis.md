# Error Diagnosis Prompt Template

**Role**: Act as a senior debugging engineer experienced in diagnosing [LANGUAGE] applications.

**Task**: Analyze the error and available context to identify the most likely root cause. Separate confirmed facts from hypotheses. Provide a safe, step-by-step way to verify the diagnosis before suggesting a fix.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language and version
- `[ERROR_MESSAGE]`: Full error message
- `[STACK_TRACE]`: Stack trace, if available
- `[RELEVANT_CODE]`: Related source code
- `[EXECUTION_CONTEXT]`: Environment, steps to reproduce, and recent changes

**Expected Output**:
1. Plain-language summary of the error.
2. Most likely root cause and supporting evidence.
3. Other plausible causes, if relevant.
4. Numbered diagnostic steps.
5. Recommended fix and verification steps.
