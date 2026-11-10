# Prompt Use Cases

This document identifies common use cases where reusable AI prompt patterns can improve software development workflows. The use cases are organized into five categories covering code quality, debugging, documentation, testing, and code understanding.

## 1. Code Quality

- **Code Refactoring**
  - **Goal**: Improve code readability, maintainability, and performance without changing its existing behavior.
  - **Input**: Source code in [LANGUAGE] and optional refactoring requirements.
  - **Output**: Refactored code with an explanation of the improvements.

- **Code Review**
  - **Goal**: Identify potential code quality issues, security risks, and violations of coding best practices.
  - **Input**: Source code, programming language, and relevant coding standards.
  - **Output**: A list of identified issues, their severity, and recommended solutions.

- **Style Enforcement**
  - **Goal**: Ensure consistent naming conventions, formatting, and coding standards across a project.
  - **Input**: Source code and the required style guidelines.
  - **Output**: Updated code following the specified conventions.

## 2. Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of an error and explain why it occurs.
  - **Input**: Error message, stack trace, relevant source code, and execution context.
  - **Output**: Explanation of the root cause and recommended steps to fix the issue.

- **Bug Fixing**
  - **Goal**: Find and fix bugs while preserving the existing functionality.
  - **Input**: Source code, bug description, and expected behavior.
  - **Output**: Corrected code with an explanation of the changes.

- **Performance Troubleshooting**
  - **Goal**: Identify performance bottlenecks such as slow database queries, memory usage, or inefficient algorithms.
  - **Input**: Relevant source code, performance metrics, and system information.
  - **Output**: Identified bottlenecks and practical optimization recommendations.

## 3. Documentation

- **Code Documentation**
  - **Goal**: Generate clear documentation that explains the purpose and behavior of code components.
  - **Input**: Source code in [LANGUAGE] and documentation format requirements.
  - **Output**: Documentation comments and explanations for functions, classes, and methods.

- **API Documentation**
  - **Goal**: Create structured documentation for REST API endpoints.
  - **Input**: API controllers, endpoint definitions, HTTP methods, request and response models.
  - **Output**: API documentation including endpoints, parameters, request examples, response examples, and status codes.

## 4. Testing

- **Unit Test Generation**
  - **Goal**: Generate unit tests that verify individual functions and methods.
  - **Input**: Source code, programming language, and preferred testing framework.
  - **Output**: Unit test cases covering normal scenarios, edge cases, and expected failures.

- **Test Case Design**
  - **Goal**: Identify different scenarios to validate a feature or requirement.
  - **Input**: Feature description, business requirements, and expected behavior.
  - **Output**: Structured test cases with inputs, expected results, and test conditions.

- **Test Coverage Analysis**
  - **Goal**: Identify untested code paths and areas that require additional test coverage.
  - **Input**: Source code, existing test files, and test coverage report.
  - **Output**: A coverage analysis with missing test scenarios and recommendations for additional tests.

## 5. Code Understanding & Development

- **Code Explanation**
  - **Goal**: Understand complex code, unfamiliar methods, or existing application architecture.
  - **Input**: Source code, programming language, and specific questions about its behavior.
  - **Output**: A clear step-by-step explanation of the code logic, important components, and their relationships.

- **Feature Implementation**
  - **Goal**: Implement a new feature while following the existing project architecture and coding conventions.
  - **Input**: Feature requirements, existing source code, technology stack, and implementation constraints.
  - **Output**: Implementation code, an explanation of the changes, and suggested tests.

---

**Total Categories**: 5

**Total Use Cases**: 13