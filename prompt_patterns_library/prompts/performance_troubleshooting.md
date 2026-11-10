# Performance Troubleshooting Prompt Template

**Role**: Act as a performance engineer experienced in profiling and optimizing [APPLICATION_TYPE] systems.

**Task**: Examine the supplied code and performance evidence to identify likely bottlenecks. Prioritize recommendations by expected impact and implementation effort. Do not claim that a change improves performance without explaining how it should be measured.

**Input Placeholders**:
- `[APPLICATION_TYPE]`: Application or system type
- `[LANGUAGE_AND_STACK]`: Language, frameworks, and runtime versions
- `[CODE_BLOCK]`: Relevant code
- `[PERFORMANCE_METRICS]`: Timings, CPU, memory, throughput, or profiling results
- `[SYSTEM_CONTEXT]`: Hardware, workload, and environment
- `[CONSTRAINTS]`: Compatibility or resource constraints

**Expected Output**:
1. Summary of observed performance concerns.
2. Potential bottlenecks with evidence and confidence level.
3. Prioritized recommendations, including trade-offs.
4. Example code changes where appropriate.
5. A measurement plan to compare performance before and after changes.
