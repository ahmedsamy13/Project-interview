# Quality coverage proportional to the project

Use this at blueprint time, on material scope changes, and before release. It is a coverage map, not a claim of a complete security audit. Select controls from the project's platform, data, exposure, and business rules. If a domain needs specialist knowledge, identify the gap and research or recommend appropriate review.

For each relevant concern, record **requirement / applicability / timing / verification / evidence** in the brief or architecture. Timing is `now`, `before release`, `later`, or `not applicable` with a reason. Important unknowns stay visible. Never downgrade a necessary protection to optional merely because the project is an MVP.

| Concern | Decisions to make | Example evidence or check |
|---|---|---|
| Core correctness | Business invariants, edge cases, accepted input, error behavior | Valid, invalid, boundary, and conflicting actions produce expected outcomes |
| Identity and access | Authentication, session lifecycle, recovery, role and record/tenant permissions | Another user or tenant cannot read or change a private record; expiry/revocation works |
| Trust boundaries | Server-side validation, safe queries, output handling, browser/request protections as applicable | Crafted inputs and unauthorized requests fail safely; client checks are not the only checks |
| Sensitive data | Collection minimization, secrets, encryption needs, retention, deletion, export, log redaction | No secret in client bundles/history; deletion and data-access behavior checked |
| Abuse and dependencies | Upload limits, rate limits, resource budgets, dependency maintenance | Oversized or repeated requests are bounded; known issues reviewed in context |
| Data consistency | Uniqueness, transactions/atomic operations, idempotency, concurrency | Simultaneous booking or repeated delivery does not violate the invariant |
| External services | Timeouts, bounded retries, webhook verification, duplicates, degraded behavior | Service outage or duplicate event cannot silently corrupt state |
| User experience | Loading, empty, error, success, cancellation, retry, responsive behavior | Main workflow works across relevant screen sizes and failure states |
| Accessibility | Semantic controls, labels, keyboard navigation, focus, contrast, clear errors | Keyboard walkthrough and appropriate automated/manual checks |
| Localization | Languages, RTL, dates, time zones, currencies, units where needed | Date/time and input behavior matches stated user expectations |
| Performance and scale | Realistic load, query patterns, payload limits, indexes, capacity assumptions | Measure target latency/throughput with stated data and concurrency; investigate bottlenecks |
| Reliability and recovery | Partial failure, backups, restore, offline sync, acceptable loss/downtime | Restore drill or recovery scenario, not merely "backups enabled" |
| Testing | Unit tests for rules, integration at boundaries, critical end-to-end journeys | Checks reproduce meaningful failures and are tied to acceptance criteria |
| Delivery | Environments, config validation, schema migrations, CI, release/rollback | Fresh setup works; migration and rollback/recovery plan exercised appropriately |
| Operations and cost | Actionable logs, metrics, error reporting, maintenance, spending limits | Detect a representative failure without exposing private data; budget assumptions recorded |
| Documentation | Setup, config examples without secrets, architecture, usage, recovery | Another developer can run the project and locate the important decisions |

## Conditional depth

- **Private/local prototype:** minimize infrastructure; still address data loss, secrets, and relevant input/filesystem risks. State what changes before public exposure.
- **Shared application:** include identity/permissions when needed, abuse controls, deployment configuration, and recovery. Define release checks instead of claiming "production ready."
- **Multi-tenant or high-concurrency system:** explicitly assess isolation, resource contention, audit needs, consistency, and capacity. Do not infer microservices from the word "scale."
- **Payments, health, or other sensitive domains:** use proven service boundaries and establish the need for specialist review; never promise legal compliance or complete security certification.
- **AI functionality:** define permitted actions, untrusted content boundaries, validation of structured output, representative evaluations, fallback behavior, privacy, and usage/cost limits. A model response is not evidence that an external action succeeded.

Security checks should connect a concrete asset and threat to a control and verification method. Performance claims require measurements. Record observed evidence separately from planned tests and user-reported results.

## Primary references

These are starting points, not mandatory hosting providers or a substitute for current stack documentation. Consult the relevant official page when making specific claims and record the date consulted.

- [OWASP ASVS](https://owasp.org/projects/asvs): application security requirements and verification.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/): implementation-specific security guidance; choose only relevant sheets.
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/): accessibility requirements and supporting resources.
- [AWS Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html): architecture questions spanning operations, security, reliability, performance, cost, and sustainability; apply principles without defaulting to AWS.

Do not claim a standard has been satisfied without choosing the applicable scope and actually evaluating it.
