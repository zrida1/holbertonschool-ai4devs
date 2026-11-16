# Architecture Plan

## Project: AI Network Troubleshooting Assistant

## 1. Architecture Overview

The application will use a three-layer architecture consisting of:

1. **Frontend Layer** – React user interface.
2. **Backend Layer** – Java Spring Boot REST API.
3. **Data and AI Services Layer** – MySQL database and external AI API.

The frontend communicates with the backend through REST APIs. The backend validates requests, communicates with the AI service, and stores the results in MySQL.

## 2. Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | React |
| Backend | Java, Spring Boot |
| API Communication | REST API, JSON |
| Database | MySQL |
| AI Integration | OpenAI API |
| Version Control | Git, GitHub |
| Deployment | Render / Vercel |
| Testing | JUnit, Mockito, Jest |

## 3. Main Components

### Frontend
- Provides a form for entering network problems.
- Displays AI-generated analysis.
- Shows troubleshooting instructions.
- Allows users to view previous requests.
- Displays loading states and error messages.

### Backend
- Exposes REST API endpoints.
- Validates incoming user requests.
- Manages troubleshooting requests.
- Communicates with the AI service.
- Saves analysis results and troubleshooting steps.
- Retrieves previous analyses.

### AI Service
- Receives network problem descriptions.
- Analyzes the reported symptoms.
- Identifies possible causes.
- Generates troubleshooting instructions.
- Returns structured results to the backend.

### Database
- Stores user information.
- Stores troubleshooting requests.
- Stores AI analysis results.
- Stores troubleshooting steps.

## 4. Request Workflow

1. The user enters a network problem in the React application.
2. The frontend sends a POST request to the Spring Boot backend.
3. The backend validates the input.
4. The backend creates a troubleshooting request in MySQL.
5. The backend sends the problem description to the AI service.
6. The AI service returns possible causes and troubleshooting steps.
7. The backend saves the analysis and its steps in MySQL.
8. The backend returns the result to the frontend.
9. The frontend displays the analysis to the user.

## 5. Proposed REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/troubleshooting | Submit a new network problem |
| GET | /api/troubleshooting | Get previous requests |
| GET | /api/troubleshooting/{id} | Get request details and analysis |
| DELETE | /api/troubleshooting/{id} | Delete a previous request |
| GET | /api/commands/{name} | Get information about a network command |

## 6. High-Level Architecture Diagram

```text
+---------------------------+
|       React Frontend      |
|                           |
|  - Problem Input          |
|  - Analysis Results       |
|  - Request History        |
+-------------+-------------+
              |
              | REST API (JSON)
              v
+---------------------------+
|    Spring Boot Backend    |
|                           |
|  - REST Controllers       |
|  - Validation             |
|  - Business Services      |
|  - AI Integration         |
|  - Data Repositories      |
+----------+----------------+
           |
           +----------------------+
           |                      |
           v                      v
+-------------------+   +-------------------+
|    MySQL Database |   |     AI Service    |
|                   |   |                   |
|  - Users          |   |  - Problem Analysis|
|  - Requests       |   |  - Possible Causes |
|  - Results        |   |  - Suggested Steps |
|  - Steps          |   |                   |
+-------------------+   +-------------------+

```

## 7. Security and Error Handling

- Validate all incoming requests.
- Keep API keys in environment variables.
- Never expose AI API keys in the frontend.
- Handle AI service timeouts and failures.
- Return appropriate HTTP status codes.
- Restrict users to accessing their own requests if authentication is implemented.

## 8. Testing Strategy

- **Unit Testing:** Test backend services and business logic using JUnit and Mockito.
- **API Testing:** Test REST endpoints and validation behavior.
- **Frontend Testing:** Test forms and UI behavior using Jest.
- **Integration Testing:** Verify communication between the backend and MySQL.
- **AI Integration Testing:** Verify that AI responses are handled correctly, including failure cases.

## 9. Deployment Plan

- Deploy the React frontend using Vercel.
- Deploy the Spring Boot backend using Render.
- Use a managed MySQL database.
- Configure API keys and database credentials through environment variables.

## 10. MVP Scope

The initial MVP will focus on:
- Submitting network problems.
- Generating AI-powered analysis.
- Displaying possible causes and troubleshooting steps.
- Saving and viewing previous analyses.

Authentication, advanced network diagnostics, and additional features can be considered for future versions.