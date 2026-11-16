## AI Review Log

**PR:** Add Task Filtering Feature (`TaskFilter`, `TaskService.filterTasks()`)
**Reviewer tool:** Claude (three persona prompts: security, performance, maintainability)

### Inline Comments

**Security persona**
- (`TaskFilter.Builder.status`) Reject `null` or blank status values explicitly, e.g. with `Objects.requireNonNull`, instead of letting them silently match nothing.
- (`TaskFilter.Builder.build`) The `IllegalArgumentException` message for an invalid date range should not echo raw user input. Use a fixed message such as "dueAfter must not be later than dueBefore".
- (`TaskService.filterTasks`) If the filter ever comes from an HTTP request, validate and whitelist the status against the `Status` enum before building the filter. Never pass raw strings through.

**Performance persona**
- (`TaskService.filterTasks`) Filtering and sorting in one stream pipeline is fine for small lists. For large task sets, filter first and sort after, so the sort only touches matching tasks.
- (`TaskFilter.matches`) Date comparisons call `getDueDate()` repeatedly. Read it once into a local variable to avoid redundant calls.
- (`TaskService.filterTasks`) Returning `List.copyOf(...)` copies the result a second time. `Collectors.toUnmodifiableList()` gives an immutable list without the extra copy.

**Maintainability persona**
- (`Task.getDueDate`) Returning `null` for tasks without a due date pushes null checks onto every caller. Consider returning `Optional<LocalDate>`.
- (`TaskFilter`) Add Javadoc on the builder methods stating that `dueBefore` and `dueAfter` are inclusive or exclusive, since this is easy to get wrong.
- (`TaskFilterTest`) Several tests repeat the same task setup. Extract it into a `@BeforeEach` method or a small test-data factory.
- (`TaskFilterTest`) Test names should follow one convention, e.g. `filter_withStatusOnly_returnsMatchingTasks`, so failures read clearly in reports.

### Global Feedback

**Security**
- Add a test confirming that a `null` filter passed to `filterTasks` fails fast with a clear exception rather than a `NullPointerException` deep in the stream.

**Performance**
- If the task list grows large, consider moving filtering into the database query layer (e.g. a `WHERE status = ? AND due_date BETWEEN ? AND ?` clause) instead of filtering in memory.

**Maintainability**
- Recommend splitting `TaskFilter.matches` into small private methods (`matchesStatus`, `matchesDueDate`) so each criterion can be tested and extended independently, for example when adding priority or assignee filters later.
- Add a test for the boundary case where a task's due date equals `dueAfter` or `dueBefore`, to document whether the range is inclusive.
- Consider a short README or Javadoc section with a usage example of the fluent builder, so other contributors can use the feature without reading the tests.

### Summary of Findings
| Persona | Inline | Global | Total |
|---|---|---|---|
| Security | 3 | 1 | 4 |
| Performance | 3 | 1 | 4 |
| Maintainability | 4 | 3 | 7 |
| **Total** | **10** | **5** | **15** |
