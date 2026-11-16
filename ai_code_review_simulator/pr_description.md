# Pull Request: Add Task Filtering Feature

## Summary

This pull request introduces a task filtering feature that allows users to find tasks based on status, priority, deadline, and title keywords.

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

## Testing

Unit tests cover:
- Empty filters.
- Status filtering.
- Priority filtering.
- Keyword searching.
- Deadline range filtering.
- Combined filters.
- Empty search results.
- Invalid date ranges.
- Invalid task data.

Run tests using:

`mvn test`

## Implementation Details

- Language: Java 17+
- Testing Framework: JUnit 5
- Java Streams API used for filtering.
- No external database or API integration is required for this feature.

## Expected Result

Users can filter tasks efficiently using one or multiple criteria while invalid filtering configurations are rejected.