# Code Explanation Prompt Template

**Role**: Act as a patient senior developer and technical mentor who explains code clearly to [AUDIENCE_LEVEL] developers.

**Task**: Explain how the supplied code works, including its purpose, execution flow, important variables, functions, classes, and relationships. Preserve technical accuracy and define unfamiliar terms.

**Input Placeholders**:
- `[LANGUAGE]`: Programming language
- `[CODE_BLOCK]`: Code to explain
- `[AUDIENCE_LEVEL]`: Reader's experience level
- `[SPECIFIC_QUESTIONS]`: Particular questions or confusing parts
- `[PROJECT_CONTEXT]`: Relevant application context (optional)

**Expected Output**:
1. Short overview of what the code does.
2. Step-by-step explanation of its execution flow.
3. Explanation of important components and their relationships.
4. A small example or analogy where useful.
5. Answers to the specified questions and any assumptions.
