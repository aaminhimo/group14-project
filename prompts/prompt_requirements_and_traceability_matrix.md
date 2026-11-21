# Prompt Record: Requirements Specification and Traceability Matrix – Group 14

## Project information
- **Group:** 14
- **Project:** AI Energy Consumption Forecasting Dashboard
- **Course:** Software Engineering (CS13477), Fall 2026
- **AI tool:** Claude Code (desktop app), model Claude Opus 5.5
- **Version / increment:** v0.1.0-design
- **Owner:** Kareem Qasmiya (20230035)
- **Status:** Completed – merged in PR #10

## Goal
Produce the project's requirements specification (use cases, functional and non-functional requirements) and a traceability matrix that links every requirement to its design element, planned increment, implementation module and test.

## Relevant requirements and design references
- Course project instructions §3.4 (design-to-code traceability), §5.2 (use cases), §8 (mandatory `docs/` files).
- Team project plan: placeholder requirement IDs per increment (FR-01..FR-16).
- Dataset analysis of the UCI Appliances Energy Prediction data (19,735 rows, 10-minute intervals, no missing values).
- C4 container diagram and sequence diagrams SD-01..SD-05.

## Prompt / instructions given to the AI
*(Summary of the key instructions; minor interactive exchanges omitted.)*
> Following the professor's project instructions and our team project plan, analyse the UCI Appliances Energy Prediction dataset and prepare the design baseline for our dashboard. Write the requirements as Markdown with stable IDs: use cases, functional requirements mapped to our planned increments, and measurable non-functional requirements. Create the traceability matrix in the professor's recommended format (Requirement ID, Use Case / Design Element, Increment, Implementation Module, Test, Status). Base everything on verified dataset facts rather than assumptions.

## Intended output
- `docs/requirements.md`: use cases UC-01..UC-07, FR-01..FR-16 with priority and target increment, NFR-01..NFR-08 with a verification method.
- `docs/traceability_matrix.md`: one row per requirement, status "Designed".

## Acceptance criteria
- [x] Every functional requirement is testable and assigned to one increment.
- [x] Every non-functional requirement has a stated verification method.
- [x] Every requirement appears in the traceability matrix with design and test references.
- [x] Requirement IDs match the incremental development plan and the sequence diagrams.

## Corrections and decisions during review
- The dataset analysis showed that predicting the previous reading already reaches R² ≈ 0.46, so the requirements were refined to separate what-if prediction (FR-11) from next-step forecasting (FR-13), and NFR-04 requires the model to beat both baselines.
- The default alert threshold (400 Wh, FR-14) was set from the measured distribution (about the 97th percentile).

## Results and review
- **Output files:** `docs/requirements.md`, `docs/traceability_matrix.md`
- **Pull request:** #10 (`docs/requirements`). Content first produced on 2026-11-11 and re-uploaded from `backup/main-before-reset` after the agreed reset of `main`.
- **Reviewer:** _to be completed by the reviewer of PR #10_
