# Coding Benchmark Tasks

This document contains three coding tasks designed to evaluate AI coding assistants such as GitHub Copilot. Each task should take approximately 15–30 minutes to complete.

## Task 1 - Create a REST API Endpoint

**Requirements:**
- Implement a REST endpoint `POST /api/users`.
- Accept user information containing a name and email.
- Validate that both fields are provided.
- Validate the email format.
- Return an appropriate HTTP response.

**Inputs:**

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Outputs:**

Successful response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Acceptance Criteria:**
- Returns HTTP 201 Created when a user is successfully created.
- Returns HTTP 400 Bad Request when the name or email is missing.
- Returns HTTP 400 Bad Request when the email format is invalid.
- Generates a unique ID for each user.

---

## Task 2 - Find Duplicate Elements in an Array

**Requirements:**
- Write a Java method that finds duplicate integers in an array.
- Return each duplicated number only once.
- Do not modify the original array.
- Use Java Collections where appropriate.

**Inputs:**

```java
int[] numbers = {1, 2, 3, 2, 4, 5, 1, 6};
```

**Outputs:**

```java
[1, 2]
```

**Acceptance Criteria:**
- Correctly identifies all duplicate numbers.
- Each duplicate appears only once in the result.
- Returns an empty collection when there are no duplicates.
- Does not modify the original array.
- Handles an empty array and arrays containing a single element.

---

## Task 3 - SQL Query for Department Statistics

**Requirements:**
- Assume there is an `employees` table with the following columns: `id`, `name`, `department`, and `salary`.
- Write an SQL query that calculates the average salary for each department.
- Include only departments with an average salary greater than 3000.
- Sort the results by average salary in descending order.

**Inputs:**

Example table:

| id | name | department | salary |
|---|---|---|---|
| 1 | John | IT | 4000 |
| 2 | Alice | HR | 2500 |
| 3 | Bob | IT | 5000 |
| 4 | Emma | HR | 3500 |
| 5 | David | Finance | 4500 |

**Outputs:**

| department | average_salary |
|---|---|
| IT | 4500 |
| Finance | 4500 |

**Acceptance Criteria:**
- Calculates the average salary for each department.
- Excludes departments with an average salary of 3000 or less.
- Sorts results by average salary in descending order.
- Returns only the department name and average salary.