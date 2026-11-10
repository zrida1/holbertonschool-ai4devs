# Feature Implementation Prompt Template

**Role**: Act as a senior [LANGUAGE] developer familiar with the project's architecture and established coding conventions.

**Task**: Plan and implement the requested feature using the existing project structure. First identify relevant components and dependencies, then propose an implementation that satisfies the requirements. Avoid unnecessary changes and do not assume files or APIs exist unless provided.

**Input Placeholders**:
- `[FEATURE_REQUIREMENTS]`: Detailed feature description and acceptance criteria
- `[LANGUAGE_AND_TECH_STACK]`: Programming language, frameworks, and versions
- `[RELEVANT_PROJECT_FILES]`: Existing code and project structure
- `[ARCHITECTURE_AND_CONVENTIONS]`: Architectural rules and coding standards
- `[CONSTRAINTS]`: Technical, security, or compatibility constraints

**Expected Output**:
1. Brief implementation plan and files to create or modify.
2. Implementation code, organized by file.
3. Explanation of important design decisions.
4. Tests for the feature and relevant edge cases.
5. Setup, migration, or configuration steps, if required.
6. Assumptions and unresolved questions.
