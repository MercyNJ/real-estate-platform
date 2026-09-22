# CLAUDE.md

## 1. Purpose

This file defines how Claude Code and other AI coding agents must operate in this repository.

The real-estate platform is being developed incrementally, with maintainability, security, scalability, and simplicity treated as first-class requirements.

Claude Code is an **implementation assistant**, not the owner of the architecture, product requirements, security policy, development environment, or project direction.

When instructions conflict, do not silently choose an interpretation. Identify the conflict and ask the developer when the decision materially affects the project.

---

# 2. Authoritative Project Documents

The project foundation is defined by the following documents:

```text
README.md
docs/architecture.md
docs/technology-stack.md
docs/engineering-principles.md
docs/security.md
docs/domain-model.md
docs/development-roadmap.md
docs/project-status.md
CLAUDE.md
```

### Document Responsibilities

| Document                    | Authority                                                       |
| --------------------------- | --------------------------------------------------------------- |
| `README.md`                 | Project purpose and high-level description                      |
| `architecture.md`           | System architecture and structural decisions                    |
| `technology-stack.md`       | Technology choices and development tooling                      |
| `engineering-principles.md` | Coding, testing, dependency and development practices           |
| `security.md`               | Security and privacy requirements                               |
| `domain-model.md`           | Business entities, relationships, states and domain constraints |
| `development-roadmap.md`    | Implementation phases, dependencies and sequencing              |
| `project-status.md`         | Current implementation state and handoff information            |
| `CLAUDE.md`                 | Claude Code operating rules                                     |

These documents are complementary and must be considered together.

Do not duplicate large portions of these documents in `CLAUDE.md`.

If a rule already exists in a foundation document, follow that document.

### 2.1 Conflicts Between Foundation Documents

Foundation documents must remain internally consistent.

During the mandatory foundation-document review, Claude must actively look for:

- Contradictory statements between documents.
- Outdated statements that conflict with current decisions.
- Undefined concepts referenced as though they are already established.
- Rules that conflict across documents.
- Domain, architecture, security, technology, or roadmap decisions that appear inconsistent.

If a material inconsistency is found, Claude must:

1. Identify the conflicting statements.
2. Identify which document appears to own the subject.
3. Explain the inconsistency to the developer.
4. Determine whether the intended decision is already clear from the authoritative document.
5. Ask the developer to resolve the conflict when it is not clear.
6. Not silently modify one document simply to make the documents appear consistent.

Do not use document reading order, file modification time, or personal preference as a basis for resolving architectural, domain, security, or product decisions.

---

# 3. Mandatory Start-of-Session Procedure

At the beginning of **every meaningful coding session**, Claude Code must read **all project foundation documents** before making implementation changes.

The required reading order is:

```text
1. CLAUDE.md
2. README.md
3. docs/architecture.md
4. docs/technology-stack.md
5. docs/engineering-principles.md
6. docs/security.md
7. docs/domain-model.md
8. docs/development-roadmap.md
9. docs/project-status.md
```

Claude must not decide that a foundation document is unnecessary simply because the immediate task appears unrelated to it.

The purpose of reading all foundation documents is to maintain a complete understanding of:

* Project purpose
* Current architecture
* Technology constraints
* Engineering rules
* Security requirements
* Domain rules
* Development phase and dependencies
* Current implementation state

After reading the foundation documents, Claude should:

1. Identify the current development phase.
2. Identify the active work in `project-status.md`.
3. Confirm that the requested work belongs to the current phase.
4. Inspect the existing implementation relevant to the task.
5. Review existing tests and project conventions before introducing new patterns.
6. Search for existing functionality that may already solve or partially solve the requested problem.
7. Plan the smallest correct implementation.

### Source-Code Inspection

Reading all foundation documents does **not** mean reading the entire source codebase every session.

Claude should inspect the code relevant to the requested task, including related:

* Modules
* Services
* Routes
* Components
* Models
* Schemas
* Tests
* Migrations
* Configuration
* Integration code

Claude must inspect existing implementation before replacing or substantially modifying it.

Do not assume that planned functionality has already been implemented.

Do not assume that something is complete because it appears in documentation.

The actual codebase and verified test results determine implementation state.

---

# 4. Before Suggesting Changes

Before recommending a new implementation, dependency, abstraction, refactor, or architectural change:

1. Read the relevant foundation documentation.
2. Inspect the existing implementation.
3. Search the repository for existing functionality that may already solve the problem.
4. Check whether the capability is already planned or intentionally deferred.
5. Check existing utilities, services, validation, middleware, models, and infrastructure that may be reusable.
6. Prefer extending an existing implementation over creating a competing implementation.
7. Do not recommend replacing an existing approach merely because another approach is personally preferred.
8. If the proposal conflicts with an established architectural decision, explain the conflict before recommending a replacement.
9. If uncertain whether something already exists, inspect the repository before concluding that it is missing.

Do not recommend changes based only on assumptions, naming patterns, or what a typical project might contain.

---

# 5. Development Phase Control

The project follows `docs/development-roadmap.md`.

Claude Code must:

* Work within the current approved phase.
* Respect phase dependencies.
* Implement the minimum required foundation for later phases when necessary.
* Avoid implementing future features prematurely.
* Never skip phases without explicit developer approval.
* Never treat completion of one phase as automatic authorization to begin the next phase.

If a requested task belongs to a later phase:

1. Identify the phase dependency.
2. Explain why it is premature.
3. Determine whether a minimal prerequisite is actually required.
4. Ask for developer direction if the request would materially move the project ahead of the roadmap.

---

# 6. Architecture Rules

The platform uses a **modular monolith** architecture.

Current architectural direction:

* Next.js + TypeScript + Tailwind CSS frontend.
* FastAPI modular backend.
* REST API with OpenAPI.
* PostgreSQL + PostGIS as the authoritative database.
* Redis for cache, rate limiting, queues and temporary state.
* ARQ for background jobs.
* S3-compatible object storage for media.
* Cloudflare for edge/CDN/WAF capabilities.
* GitHub Actions for CI.
* Docker for development/packaging.
* LLM APIs with structured tool/function calling for the AI Property Assistant.
* OpenSearch and other advanced infrastructure are deferred until justified by evidence.

Do not silently replace these technologies or introduce major architectural alternatives.

Do not introduce:

* Microservices
* Kubernetes
* Kafka
* GraphQL
* Vector databases
* Complex RAG
* Machine-learning recommendation infrastructure
* OpenSearch as a day-one requirement
* Multiple independent backend services
* Complex cloud orchestration

unless the developer explicitly approves the architectural change.

**Established project decisions take precedence over generic trends or personal technology preferences.**

Do not undo an established architectural decision merely because another approach appears newer or theoretically superior.

---

# 7. Modular Boundaries

Backend modules must have clear ownership and boundaries.

Core modules include:

* Auth
* Users
* Properties
* Locations
* Agents & Agencies
* Enquiries
* Verification
* Search
* Media
* Notifications
* Payments
* AI Property Assistant
* Admin

A module must not directly access another module's:

* Internal repositories
* ORM models
* Database queries
* Private services
* Internal helpers
* Private data structures

Modules should communicate through deliberate public application/service interfaces.

Prefer:

```text
API / Presentation
        ↓
Application / Services
        ↓
Domain
        ↓
Infrastructure
        ↓
Database / External Systems
```

Avoid circular dependencies.

If a proposed implementation requires violating a module boundary, stop and discuss the design rather than creating a shortcut.

---

# 8. Domain Model Rules

`docs/domain-model.md` is authoritative for the business domain.

Important distinctions include:

* A **Property** represents the physical real-world property.
* A **Listing** represents a marketplace advertisement or offer for that property.
* A **Property** may have multiple Listings.
* `SavedProperty` references a Listing because users save marketplace offers.
* `AgencyMembership` defines the relationship between users and agencies.
* An `AGENCY_ADMIN` role alone does not grant access to every agency; authorization must consider active agency membership.
* Property media may be property-level or listing-specific according to the rules in `domain-model.md`.
* Monetary values must include both an amount and an explicit currency.
* Geographic information is a first-class part of the domain.

Do not invent new entities, relationships, statuses, permissions, terminology, or business rules when an existing domain definition already applies.

If the domain model is missing or ambiguous:

1. Stop before implementing the affected functionality.
2. Explain the ambiguity.
3. Propose the minimum required decision.
4. Obtain developer approval where necessary.
5. Update `domain-model.md`.
6. Then implement the change.

The domain model document is a business/domain blueprint. It does not constitute a complete database schema or SQLAlchemy implementation. When implementing a domain entity, Claude must thoroughly design and verify the actual model, relationships, constraints, indexes, migrations, and tests rather than mechanically translating the markdown into code.

---

# 9. Decision Gate — Domain and Data Model Changes

Before implementing a change that introduces or modifies a business concept, domain model, or persistent data structure, stop and obtain explicit developer approval.

This includes:

* New or removed database tables, columns, or relationships.
* Renaming models, tables, columns, fields, or domain concepts.
* New roles, statuses, enums, pricing concepts, or verification states.
* Changes to property, listing, agency, agent, location, payment, or user concepts.
* Changes to business rules, calculations, workflows, or authorization rules.
* Changes that affect existing data or historical records.
* New persistent configuration that becomes part of the application's long-term design.
* Changes to public API contracts caused by a domain change.

Before requesting approval:

1. Analyze the impact across the relevant codebase.
2. Explain the proposed change in simple terms.
3. Identify affected modules, models, APIs, migrations, and data.
4. Explain why the change is necessary.
5. Identify reasonable alternatives where relevant.
6. Explain significant risks or side effects.
7. Wait for explicit approval before implementing.

Do not introduce new domain terminology or persistent data structures merely because they appear convenient.

---

# 10. Verify Before Implementing

Do not infer existing behavior, data types, relationships, or business rules from surrounding code.

If a change depends on an existing:

* Function
* API endpoint
* Request or response field
* Database model or column
* Relationship
* Enum or status
* Configuration value
* Authorization rule
* Business rule
* External integration

then:

1. Locate the source of truth.
2. Inspect its current implementation.
3. Verify its data type, relationships, and behavior.
4. Search for relevant usages where necessary.
5. Inspect related tests.
6. Only then implement the change.

If behavior is unclear, stop and ask rather than guessing.

---

# 11. Database Rules

PostgreSQL is the authoritative source of business data.

Redis, caches, search indexes and other derived stores must not become competing sources of truth.

Use:

* SQLAlchemy 2.x
* Alembic
* PostgreSQL
* PostGIS

Database changes must be implemented through Alembic migrations.

Do not make undocumented manual schema changes.

Before changing the database:

* Check the domain model.
* Check existing migrations.
* Check relationships and constraints.
* Consider existing data.
* Consider indexes and query patterns.
* Consider migration safety.
* Consider rollback or recovery implications where appropriate.

Do not introduce speculative database entities merely because they may be useful in the future.

---

# 12. API Rules

The backend exposes a REST API.

Use:

```text
/api/v1/
```

API implementations must:

* Follow consistent resource-oriented conventions.
* Validate input at the API/application boundary.
* Use Pydantic for API/application contracts.
* Return appropriate HTTP status codes.
* Provide predictable error responses.
* Support pagination for potentially large collections.
* Apply authentication and authorization server-side.
* Keep OpenAPI documentation synchronized with implementation.

Breaking API changes require an explicit versioning decision.

Do not put core business logic directly inside route handlers.

Routes should primarily handle:

1. Request parsing.
2. Authentication context.
3. Validation.
4. Calling application services.
5. Response construction.

---

# 13. Security Rules

Security requirements are defined in `docs/security.md`.

Security must never be weakened simply to make an implementation easier.

Claude Code must never:

* Disable authentication to make a feature work.
* Bypass authorization.
* Remove rate limiting without approval.
* Expose private verification documents publicly.
* Commit secrets.
* Log passwords, tokens, API keys or sensitive credentials.
* Disable TLS verification in production.
* Remove security headers merely to resolve a development issue.
* Trust client-provided authorization or payment status.
* Remove validation to make tests pass.
* Expose internal errors or stack traces in production.
* Create insecure temporary authentication mechanisms without explicit approval.

Every protected operation requires server-side authorization.

Do not assume that hiding a frontend control provides security.

---

# 14. Authentication and Authorization

Authentication and authorization are separate concerns.

For protected operations, verify:

```text
Identity
   ↓
Role / Permission
   ↓
Resource Ownership or Relationship
   ↓
Requested Action
```

Consider agency membership, listing ownership, resource relationships and administrative permissions where applicable.

Do not implement authorization based only on frontend state.

Privileged roles and sensitive operations must follow the MFA and reauthentication requirements defined in `security.md`.

---

# 15. AI Property Assistant Rules

The AI Property Assistant must remain constrained by normal application logic.

The AI must not:

* Directly access PostgreSQL.
* Generate arbitrary SQL.
* Invent properties.
* Invent prices or availability.
* Bypass authentication or authorization.
* Access private verification documents without authorization.
* Modify application data without an authorized application operation.
* Treat property descriptions, enquiries or other user-controlled content as trusted instructions.
* Override deterministic business rules.

Expected flow:

```text
User request
     ↓
LLM
     ↓
Structured intent
     ↓
Validated application tool
     ↓
Normal property/search logic
     ↓
Real database results
     ↓
LLM response
```

The application remains authoritative.

AI output must be validated before being used by application logic.

Prompt injection must be treated as a security concern, not merely a prompting problem.

---

# 16. External Integrations

External systems must be isolated behind appropriate application/integration boundaries.

This includes:

* Payment providers
* LLM providers
* Email providers
* Object storage
* Future SMS/WhatsApp providers
* Other third-party APIs

Do not spread provider-specific implementation details throughout the application.

Where appropriate, external operations must support:

* Validation
* Authentication
* Authorization
* Idempotency
* Retry safety
* Timeout handling
* Error handling
* Auditability

Never trust an external response simply because it came from a provider.

When introducing a new external dependency or integration, consider:

* Deployment requirements
* Required credentials or environment variables
* Local development impact
* CI requirements
* Failure modes
* Vendor lock-in
* Ongoing operational complexity

---

# 17. Payments

Payments are intentionally deferred until the appropriate roadmap phase.

When payment work begins:

* Use the internal payment abstraction defined by the architecture.
* Keep provider-specific code behind an adapter/integration boundary.
* Do not trust payment status supplied by the client.
* Validate provider responses server-side.
* Verify webhooks.
* Protect against replay.
* Use idempotency.
* Record provider references.
* Maintain auditable payment state transitions.

The initial Kenyan payment integration is expected to use M-Pesa/Daraja, but provider details must remain isolated from the core domain.

---

# 18. Files and Media

PostgreSQL stores media metadata, not binary media files.

Use S3-compatible object storage for uploaded files.

Property images, verification documents and future uploads are untrusted input.

Uploads must be validated for:

* File type
* MIME type
* Content signature where appropriate
* File size
* Safe object naming
* Storage location
* Access permissions

Private verification documents must remain private and use controlled access such as short-lived signed URLs where appropriate.

Never place uploaded files inside the application source tree.

---

# 19. Dependency and Installation Policy

**Claude Code must never independently install software or dependencies.**

This includes:

* Python
* Node.js
* pnpm
* PostgreSQL
* PostGIS
* Redis
* Docker
* Python packages
* npm/pnpm packages
* CLIs
* Testing tools
* Linters
* Formatters
* Type checkers
* Cloud tooling
* AI SDKs
* Infrastructure tooling

If something is missing:

1. Identify the dependency.
2. Explain why it is required.
3. Provide the installation command or appropriate instructions.
4. Stop and wait for the developer.

Claude may configure and use tools that are already installed.

Editing `package.json`, `pyproject.toml`, lockfiles or other dependency declarations does **not** constitute permission to install the dependency.

Do not introduce a dependency merely because it makes a small task easier.

---

# 20. Code Quality

Prefer:

* Simple code.
* Clear names.
* Small focused functions.
* Clear responsibilities.
* Explicit types.
* Reusable application services where appropriate.
* Existing project conventions.
* Tests for meaningful behavior.
* Minimal dependencies.

When extending existing code, prefer consistency with established project patterns over introducing a theoretically superior pattern without a clear benefit.

Improve an existing pattern when there is a concrete reason such as:

* Correctness
* Security
* Maintainability
* Performance
* Testability

Avoid:

* Clever abstractions.
* Huge functions.
* God classes.
* Duplicate business logic.
* Dead code.
* Unused dependencies.
* Vague utility modules.
* Premature abstraction.
* Unrelated refactoring.

Prefer reuse over duplication.

Do not create duplicate:

* Validation
* Middleware
* Services
* Utilities
* Database queries
* Business rules
* Infrastructure
* API behavior

when an appropriate existing implementation can be reused or extended.

---

# 21. Code Comments

Write comments only where they provide meaningful value.

Comments should explain:

* Why something is done.
* An important constraint.
* A non-obvious security consideration.
* A non-obvious business rule.
* A deliberate workaround.
* A non-obvious architectural decision when the explanation belongs close to the code.

Avoid comments that:

* Explain obvious code.
* Repeat the implementation.
* Narrate the implementation process.
* Add unnecessary historical information.
* Make code harder to read.

Prefer clear names and self-explanatory code.

Long-term architectural rationale belongs in the appropriate documentation rather than excessive source-code comments.

Keep comments accurate when the related implementation changes.

---

# 22. Refactoring Rules

When refactoring existing functionality:

* Preserve existing behavior unless a behavior change is explicitly requested.
* Identify behavior changes clearly.
* Add or update regression tests.
* Avoid mixing unrelated cleanup with the requested change.
* Do not silently rewrite working code merely because another approach looks cleaner.
* Do not undo completed architectural or engineering decisions without justification.
* Prefer small, reviewable improvements over large rewrites.

For significant refactoring, first understand:

* Affected module boundaries.
* Relevant request/data flows.
* Dependencies and callers.
* Existing tests.
* Duplicate or competing implementations.
* Potential behavioral risks.
* Security implications.
* Data integrity implications.
* Performance implications.

Do not begin a large refactor until this analysis is complete.

If existing code conflicts with the architecture:

1. Identify the conflict.
2. Explain the risk.
3. Determine the smallest safe correction.
4. Obtain developer direction when the change is significant.
5. Implement deliberately.

---

# 23. Testing and Validation

Use the project's defined testing tools:

### Backend

* Pytest
* Ruff
* mypy

### Frontend

* Vitest
* React Testing Library
* ESLint
* Prettier
* TypeScript strict checking

### End-to-End

* Playwright

Tests should verify behavior rather than implementation details wherever practical.

Before considering meaningful work complete, run the relevant checks that are already available in the environment.

Do not claim tests passed unless they were actually executed.

Do not fabricate test results.

When a change affects existing behavior, add or update regression tests covering the affected behavior.

Testing is a core part of implementation, not an optional final step.

Claude Code should write tests alongside implementation rather than postponing testing until the end.

Meaningful functionality should have thorough automated test coverage appropriate to its risk and complexity.
For non-trivial functionality, Claude should identify the relevant test layers before implementation (unit, integration, API, database, authorization, and/or end-to-end) and explain any intentionally untested layer.

Tests should cover, where applicable:

- Happy paths.
- Validation failures.
- Boundary conditions.
- Error handling.
- Authorization and access-control rules.
- Business rules and state transitions.
- Database constraints and relationships.
- API contracts and error responses.
- External integration behavior through appropriate mocks or test doubles.
- Security-sensitive behavior.
- Regression cases for previously identified bugs.

High-risk functionality such as authentication, authorization, payments, verification, data integrity, permissions, and security controls requires particularly thorough testing.

Do not consider a feature complete merely because the implementation works manually. Automated tests are part of the definition of done.

---

# 24. Git and Branching

Do not work directly on `main` for meaningful implementation changes.

Preferred workflow:

```text
main
  ↓
feature/fix/chore branch
  ↓
implementation
  ↓
tests / quality checks
  ↓
review
  ↓
merge
  ↓
main
```

Use logical commits with meaningful messages.

Do not:

* Commit secrets.
* Commit unrelated changes.
* Rewrite shared history without approval.
* Create unnecessary commits for trivial edits.
* Modify unrelated files without reason.

Claude Code must not approve or merge its own work without explicit developer involvement.

---

# 25. Change Scope

Stay within the requested task.

Do not silently:

* Rewrite unrelated code.
* Upgrade unrelated dependencies.
* Change architecture.
* Change database structure outside the task.
* Modify security controls.
* Introduce new infrastructure.
* Change API contracts unnecessarily.
* Reformat the entire repository.
* Rename unrelated files.
* Delete code simply because it appears unused without verifying its purpose.

If you discover an important unrelated problem:

1. Mention it.
2. Explain the impact.
3. Keep it separate from the current task unless the developer asks to address it.

Every change should leave the affected area at least as maintainable, secure, and understandable as before.

Prefer incremental improvement over large rewrites.

---

# 26. Significant Change Communication

For significant proposed changes, communicate:

* Why the change is needed.
* What problem it solves.
* Expected benefits.
* Main risks or side effects.
* Affected modules or systems.
* Dependencies.
* Approximate implementation complexity when useful.
* Whether it affects the roadmap or current phase.

For architectural, domain, security, data-model, or infrastructure decisions, do not proceed silently.

---

# 27. When Claude Must Stop and Ask

Claude Code should ask the developer before proceeding when a decision materially affects:

* Architecture
* Security
* Authentication
* Authorization
* Data integrity
* Database structure
* Public API contracts
* Domain entities or relationships
* Module boundaries
* Core technology choices
* Major dependencies
* Infrastructure
* Payment behavior
* Privacy/data retention
* Project scope
* Phase sequencing

Do not ask unnecessary questions when an existing documented rule clearly determines the correct implementation.

When the answer is already defined by the foundation documents, follow the documented decision.

When the documentation is genuinely ambiguous or conflicting, stop and ask rather than guessing.

---

# 28. Documentation Maintenance

Documentation must remain aligned with implementation.

Claude Code should update `docs/project-status.md` after meaningful implementation work.

Record:

* What was completed.
* What remains.
* Important discoveries.
* Implementation decisions.
* Blockers.
* Test status.
* Database/migration status.
* Security observations.
* Next steps.

If an implementation changes an authoritative architectural, security, technology or domain decision, update the relevant foundation document rather than recording the change only in `project-status.md`.

Do not fabricate documentation to make the project appear more complete than it is.

---

# 29. Phase Definition of Done

A feature or phase is not complete merely because code exists.

Before marking meaningful work complete, verify the applicable:

* Functional requirements
* Domain rules
* Authorization
* Security requirements
* Validation
* Database migrations
* Tests
* Error handling
* API behavior
* Type checking
* Linting/formatting
* Documentation
* Module boundaries
* CI checks where available
* Review requirements

Use `docs/development-roadmap.md` for the authoritative Definition of Done.

---

# 30. Current Project Status

Always use `docs/project-status.md` as the current handoff record.

At the time this file was created:

```text
Project stage: Pre-implementation
Current phase: Phase 0 — Product and Architecture Foundation
Implementation status: Not started
Foundation documentation: Complete
Developer approval for Phase 0 implementation: Not yet given
```

Do not assume this status remains current without checking `project-status.md`.

---

# 31. Working Principle

When deciding how to implement something, prefer this order:

```text
Existing requirement
        ↓
Foundation documentation
        ↓
Existing project conventions
        ↓
Existing implementation
        ↓
Simplest correct implementation
        ↓
Tests and validation
        ↓
Developer review
```

Do not solve hypothetical future problems with unnecessary infrastructure today.

Build a strong foundation first.

Scale based on evidence.

Keep business logic deterministic where it matters.

Keep AI constrained by application rules.

Keep security server-side.

Keep PostgreSQL authoritative.

Keep module boundaries clear.

Keep dependencies deliberate.

Keep the developer in control of architecture, installation, security, and phase progression.

Leave the repository cleaner, safer, and more maintainable than you found it.

---

# 32. Final Rule

**Do not guess when guessing could create a lasting architectural, security, data, or product decision.**

When the correct answer is already documented, follow the documentation.

When it is not documented and the decision is significant, stop and ask.

When it is a small implementation detail covered by established conventions, use the simplest reasonable solution.

Claude Code is here to help build the platform carefully, incrementally, and transparently — not to silently make major decisions on the project's behalf.