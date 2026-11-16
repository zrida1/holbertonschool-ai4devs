# Pull Request: Add Task Filtering Feature

## Summary
Implements task filtering by status and due date in the Java task manager. Adds a new `TaskFilter` class with a fluent builder and exposes it through `TaskService.filterTasks()`. Callers can now retrieve only the tasks that match a given status and/or fall within a due-date range, instead of loading and filtering the full list manually.

## Changes
- Added `TaskFilter.java` with a builder (`status`, `dueBefore`, `dueAfter`) and a `matches(Task)` method
- Added `filterTasks(TaskFilter filter)` to `TaskService.java`, returning an immutable, sorted-by-due-date list
- Updated `Task.java` to expose `getStatus()` and `getDueDate()` (null-safe for tasks without a due date)
- Added input validation: `dueAfter` must not be later than `dueBefore`, otherwise `IllegalArgumentException` is thrown
- Added 8 new JUnit 5 tests in `TaskFilterTest.java` covering:
  - filter by status only
  - filter by due-date range only
  - combined status + date filter
  - empty filter returns all tasks
  - no matching tasks returns an empty list
  - tasks without a due date are excluded by date filters
  - invalid date range throws `IllegalArgumentException`
  - result ordering by due date
- All existing tests continue to pass (`mvn test`)

## Context
~150 LOC (code + tests). Related issue: #42.

Motivation: clients had to fetch every task and filter it themselves, which duplicated logic and was error-prone around null due dates. Centralizing the filtering in one tested class keeps behavior consistent and makes it easy to add more criteria (priority, assignee) later.

## Testing
- Run `mvn test`: all existing and new tests pass
- Manually verified with sample data containing mixed statuses and missing due dates