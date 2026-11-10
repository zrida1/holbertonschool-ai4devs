# API Documentation Prompt Template

**Role**: Act as an API documentation specialist experienced with RESTful services and [API_SPECIFICATION].

**Task**: Produce clear API documentation from the supplied endpoint definitions and models. Describe only behavior supported by the input. Include request and response examples where enough information is available.

**Input Placeholders**:
- `[API_SPECIFICATION]`: Documentation format or standard (for example, OpenAPI)
- `[API_CODE_OR_DEFINITIONS]`: Controllers, routes, or endpoint definitions
- `[DATA_MODELS]`: Request and response models
- `[AUTHENTICATION_DETAILS]`: Authentication requirements
- `[BASE_URL]`: API base URL, if known

**Expected Output**:
1. Endpoint summary and HTTP method.
2. Path and query parameters.
3. Authentication requirements.
4. Request body schema and example.
5. Successful and error response schemas, examples, and status codes.
6. Notes about validation and relevant behavior.
