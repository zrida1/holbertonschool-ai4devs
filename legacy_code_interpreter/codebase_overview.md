# Codebase Overview – Retail Supply System (RSS)

## 1. Project Overview

The Retail Supply System (RSS) is a legacy enterprise application developed using COBOL. It was designed to support supply-related business operations and runs in a mainframe environment.

This system was documented in a Carnegie Mellon University Software Engineering Institute (SEI) modernization case study.

## 2. Age

- The system's architecture had remained largely unchanged for more than 30 years at the time of the 2001 SEI report.
- This indicates that the system originated before 1971.
- The exact initial release date is not specified in the available report.

## 3. Size

- Approximately 2 million lines of COBOL code.
- Large codebase with decades of accumulated business logic and modifications.

## 4. Main Technologies and Dependencies

- **Programming Language:** COBOL
- **Execution Environment:** Mainframe
- **System Type:** Enterprise Retail Supply System
- **Platform Dependency:** Mainframe infrastructure

The available case study does not specify exact database systems, libraries, or additional software dependencies.

## 5. Known Issues and Pain Points

- **High Technical Debt:** Decades of modifications have made the system difficult to maintain.
- **Brittle Architecture:** The system is sensitive to changes, increasing the risk of unexpected failures.
- **Limited Modernization:** Its architecture remained largely unchanged for more than 30 years.
- **Large Codebase:** Approximately 2 million lines of code make analysis and maintenance challenging.
- **Migration Complexity:** Moving such a large system to a modern architecture requires careful planning.
- **Business Continuity Risks:** Modernization must preserve existing functionality while the system continues operating.

## 6. Modernization Considerations

A gradual modernization strategy is recommended rather than replacing the entire system at once.

Possible approaches include:

- Analyzing and documenting existing business logic.
- Identifying dependencies between program components.
- Introducing automated tests before modifying critical functionality.
- Refactoring highly coupled components.
- Migrating individual modules incrementally.
- Validating the new implementation against the original system.

## 7. References

1. Carnegie Mellon University, Software Engineering Institute. *Incremental Modernization for Legacy Systems* (2001).
   https://insights.sei.cmu.edu/library/incremental-modernization-for-legacy-systems/

2. Carnegie Mellon University, Software Engineering Institute. *Legacy System Modernization Case Study*.
   https://www.sei.cmu.edu/asset_files/TechnicalReport/2001_005_001_13895.pdf