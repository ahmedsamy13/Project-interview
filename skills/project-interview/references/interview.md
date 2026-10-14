# Adaptive project interview

Use this as a coverage guide, not a questionnaire to send wholesale. Begin from the user's idea and information already available. Ask the next questions that change the plan.

## Discover in small rounds

| Round | Establish | Follow up only when it changes a decision |
|---|---|---|
| Purpose | Problem, target users, main action, expected outcome | How does the user solve it today? What would make this worth using? |
| Learner | What they can build alone, what they want to practice | Preferred hint depth, learning vs delivery priority, language, available time |
| First release | One complete useful workflow, must-have features, exclusions | Roles, permissions, business rules, observable acceptance criteria |
| Constraints | Chosen stack, device/platform, existing code, budget, deadline, team | Offline needs, SEO, distribution, integrations, deployment restrictions |
| Data and risk | Data ownership, sensitivity, retention, expected activity | Trust boundaries, concurrent writes, recovery needs, domain-specific review |
| Quality | Accessibility, performance, reliability, operations | Measurable targets where useful; unknown is better than a made-up number |

Do not require a beginner to know technical answers. Translate "scalable" into expected simultaneous activity, read/write patterns, upload sizes, and acceptable response time. Translate "secure" into assets, actors, access rules, and likely abuse. Distinguish expected users from concurrent load and measurements from estimates.

## Conditional probes

| Project signal | Questions worth investigating |
|---|---|
| Accounts or several organizations | Who owns each record? Can roles change? How are accounts recovered? Must tenants be isolated? |
| Bookings, inventory, or shared resources | What happens when two people claim the last resource? Time zones, cancellation, and overlap rules? |
| Payments or subscriptions | Who handles payment details? How do refunds, duplicate events, and delayed confirmations affect access? |
| Uploads or user-generated content | File types and sizes, visibility, retention, moderation, and abusive uploads? |
| Public content or commerce | Search discovery, rendering, accessibility, performance, and content management? |
| Mobile, desktop, CLI, or offline use | Installation/distribution, local storage, permissions, synchronization, and update strategy? |
| Real-time collaboration | Latency expectations, ordering, reconnect behavior, and conflict resolution? |
| Data processing or automation | Input quality, batch size, reproducibility, partial failure, reruns, and audit needs? |
| AI features | What may the model decide? What must be validated? Sensitive inputs, cost ceiling, failure behavior, evaluation? |
| Sensitive or regulated use | What data and jurisdiction are involved? Is specialist review needed before real users? Avoid inventing legal compliance. |

An omitted feature is not automatically required. A local learning tool may not need accounts, a server, or cloud hosting.

## Build the brief

Use [the brief template](../assets/templates/brief.md) when saving a project. Keep it concise and editable.

- Give agreed behavior IDs such as `R-001`; use `Q-001` for quality requirements.
- Express behavior through a user action, expected outcome, and failure/permission case where relevant.
- Separate confirmed facts, proposals, assumptions, and unresolved questions.
- Categorize scope as first release, later, and out of scope.
- Record learning goals separately from product requirements: practicing Express is a learner constraint, not a user feature.
- Surface contradictions instead of quietly choosing one interpretation. For example, "private entries" and "public search over all entries" need clarification.

If the user says "choose for me," recommend defaults with reasons and continue with labeled assumptions. Only block the affected decision when missing information materially changes correctness or risk. Do not keep interviewing after there is enough information for a useful provisional plan.
