# Pull Request: Add Task Filtering Feature

## Summary

This pull request introduces a Task Filtering Feature that allows users to find tasks based on status, priority, deadline, and title keywords.

The feature supports combining multiple filters to make task management easier and more efficient.

## Changes

- Added `Task.java` to represent task information.
- Added `TaskFilter.java` to define filtering criteria.
- Added `TaskFilterService.java` to implement filtering logic.
- Added status filtering (TODO, IN_PROGRESS, COMPLETED).
- Added priority filtering (LOW, MEDIUM, HIGH).
- Added deadline range filtering.
- Added case-insensitive title search.
- Added support for combining multiple filters.
- Added input validation for task and date range values.
- Added 9 JUnit 5 unit tests.

## Context and Motivation

Users may have many tasks with different priorities, statuses, and deadlines. Finding a specific task manually can become difficult.

This feature improves usability by allowing users to quickly find relevant tasks using multiple filtering criteria.

## Implementation Details

- Programming Language: Java 17+
- Testing Framework: JUnit 5
- Java Streams API used for filtering.
- Used Java Records to represent task and filter data.
- Implemented reusable filtering methods.
- No external database or API integration is required.

## LOC Evidence

The feature implementation consists of three Java source files:

1. `Task.java` – Task data model and validation.
2. `TaskFilter.java` – Filtering criteria and validation.
3. `TaskFilterService.java` – Filtering logic using Java Streams.

The target implementation size is **100–200 lines of code (LOC)**, excluding unit tests.

The implementation LOC should be verified using the source files.

## Testing

Added 9 JUnit 5 unit tests covering:

- Empty filters.
- Status filtering.
- Priority filtering.
- Keyword searching.
- Deadline range filtering.
- Combined filters.
- Empty search results.
- Invalid date ranges.
- Invalid task data.

Tests can be executed using:

`mvn test`

## Expected Result

Users can filter tasks efficiently using one or multiple criteria. The feature provides reusable filtering logic, validates invalid input, and returns only tasks matching the selected criteria.