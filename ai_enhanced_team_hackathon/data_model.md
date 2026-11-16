# Data Model

## Project: AI Network Troubleshooting Assistant

The application uses a relational database (MySQL) to store users, network troubleshooting requests, AI analysis results, and troubleshooting steps.

## 1. User

Stores information about application users.

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | BIGINT | Primary key |
| username | VARCHAR(100) | User's username |
| email | VARCHAR(150) | User's email address |
| created_at | DATETIME | Account creation date |

**Relationships:**
- One User can have multiple TroubleshootingRequests.
- One-to-Many relationship with TroubleshootingRequest.

## 2. TroubleshootingRequest

Stores network problems submitted by users.

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | BIGINT | Primary key |
| user_id | BIGINT | Foreign key referencing User |
| description | TEXT | User's network problem description |
| status | VARCHAR(30) | Request processing status |
| created_at | DATETIME | Request creation date |

**Possible Status Values:**
- PENDING
- PROCESSING
- COMPLETED
- FAILED

**Relationships:**
- Many TroubleshootingRequests belong to one User.
- One TroubleshootingRequest has one AnalysisResult.

## 3. AnalysisResult

Stores the AI-generated analysis for a troubleshooting request.

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | BIGINT | Primary key |
| request_id | BIGINT | Foreign key referencing TroubleshootingRequest |
| possible_causes | TEXT | Possible causes identified by AI |
| summary | TEXT | Short analysis summary |
| created_at | DATETIME | Analysis creation date |

**Relationships:**
- One AnalysisResult belongs to one TroubleshootingRequest.
- One AnalysisResult can have multiple TroubleshootingSteps.

## 4. TroubleshootingStep

Stores individual troubleshooting instructions.

| Field | Data Type | Description |
|-------|-----------|-------------|
| id | BIGINT | Primary key |
| analysis_id | BIGINT | Foreign key referencing AnalysisResult |
| step_number | INT | Order of the step |
| instruction | TEXT | Troubleshooting instruction |
| command_example | VARCHAR(500) | Optional network command |
| explanation | TEXT | Explanation of the command or action |

**Relationships:**
- Many TroubleshootingSteps belong to one AnalysisResult.

## Entity Relationships

```text
User (1) -------- (N) TroubleshootingRequest
                            |
                            | (1)
                            |
                            | (1)
                      AnalysisResult
                            |
                            | (1)
                            |
                            | (N)
                   TroubleshootingStep
```

## Database Notes

- MySQL will be used as the relational database.
- All entities will have primary keys.
- Foreign keys will maintain referential integrity.
- The request description and AI-generated content will be stored as text.
- A request can have one analysis result, and an analysis can contain multiple troubleshooting steps.