# User Stories

## Project: AI Network Troubleshooting Assistant

### User Story 1 – Submit a Network Problem
As a user, I want to describe my network problem so that I can receive help identifying its possible cause.

**Acceptance Criteria:**
- The user can enter a description of the network problem.
- The description cannot be empty.
- The user can submit the problem for analysis.

### User Story 2 – AI Problem Analysis
As a user, I want AI to analyze my network problem so that I can understand what might be causing it.

**Acceptance Criteria:**
- The system sends the problem description to the AI service.
- The AI returns possible causes.
- The analysis is displayed in a readable format.

### User Story 3 – Receive Troubleshooting Steps
As a user, I want to receive step-by-step troubleshooting instructions so that I can investigate and potentially solve my network problem.

**Acceptance Criteria:**
- The system provides ordered troubleshooting steps.
- Each step contains a clear explanation.
- The instructions are relevant to the reported problem.

### User Story 4 – Understand Network Commands
As a beginner, I want explanations of network commands so that I can understand how to use them.

**Acceptance Criteria:**
- The system can explain commands such as `ping`, `ipconfig`, and `nslookup`.
- Each explanation includes the command's purpose.
- Example usage is provided where appropriate.

### User Story 5 – View Previous Analyses
As a user, I want to view my previous troubleshooting requests so that I can review earlier results.

**Acceptance Criteria:**
- Previous requests are stored in the database.
- Each request displays its description and creation date.
- The user can open a previous analysis.

### User Story 6 – View Analysis Details
As a user, I want to view the complete details of an analysis so that I can review its possible causes and suggested solutions.

**Acceptance Criteria:**
- The analysis contains possible causes.
- The analysis contains troubleshooting steps.
- The details are displayed clearly.

### User Story 7 – Handle AI Service Errors
As a user, I want to receive a clear error message if the AI service is unavailable so that I know my request could not be processed.

**Acceptance Criteria:**
- The system detects AI service failures.
- A user-friendly error message is displayed.
- The application does not crash because of an AI service error.

### User Story 8 – Delete Previous Requests
As a user, I want to delete an old troubleshooting request so that I can manage my history.

**Acceptance Criteria:**
- The user can select a previous request.
- The system asks for confirmation before deletion.
- The selected request is removed from the database.

### User Story 9 – Loading Feedback
As a user, I want to see a loading indicator while AI analyzes my problem so that I know the application is processing my request.

**Acceptance Criteria:**
- A loading indicator appears after submission.
- The indicator disappears when processing finishes.
- The result or an error message is displayed afterward.

### User Story 10 – Input Validation
As a user, I want the application to validate my input so that incomplete or invalid requests are not submitted.

**Acceptance Criteria:**
- Empty descriptions are rejected.
- Input length is limited.
- Validation errors are displayed clearly.

## MVP Priority

| Priority | Features |
|----------|----------|
| High | Submit a network problem |
| High | AI problem analysis |
| High | Troubleshooting steps |
| High | Input validation |
| Medium | View previous analyses |
| Medium | View analysis details |
| Medium | Handle AI service errors |
| Low | Delete previous requests |
| Low | Network command explanations |
| Low | Loading feedback |