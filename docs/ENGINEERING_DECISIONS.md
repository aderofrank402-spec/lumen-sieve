# Engineering decisions

These concise records summarize decisions verified in the private implementation. They expose rationale and trade-offs without publishing proprietary algorithms or configuration.

## 001 — Reconcile evidence per field

**Decision:** Preserve source context and confidence at field level and reconcile competing values field by field.

**Reason:** A source can be reliable for one attribute and weak for another. Whole-record confidence hides that distinction and makes disputes difficult to investigate.

**Trade-off:** Field-level evidence increases storage, schema, API, and UI complexity.

## 002 — Separate discovery from retrieval

**Decision:** Candidate discovery produces URLs and identity signals; dedicated fetch services retrieve content.

**Reason:** Discovery and network retrieval have different scaling, safety, retry, and observability requirements.

**Trade-off:** The boundary adds RPC contracts and orchestration overhead.

## 003 — Use tiered retrieval

**Decision:** Start with a direct retrieval tier and escalate selected cases to a browser-backed tier.

**Reason:** Browser execution is more expensive and operationally complex than direct retrieval, but some sources require it.

**Trade-off:** Escalation policy and failure classification must remain observable and testable.

## 004 — Prefer deterministic reconciliation

**Decision:** Apply credibility, freshness, identity, grouping, and field rules before bounded model-assisted arbitration.

**Reason:** Deterministic layers are cheaper to reproduce, explain, test, and audit.

**Trade-off:** Rules require maintenance as source behavior and product requirements evolve.

## 005 — Make unresolved a valid outcome

**Decision:** Model no-evidence and unresolvable-conflict states explicitly.

**Reason:** A forced value can appear complete while being less trustworthy than an honest gap.

**Trade-off:** Consumers must handle null or unresolved fields instead of assuming completeness.

## 006 — Version resolved profiles

**Decision:** Persist profile versions and expose history rather than overwriting the only copy.

**Reason:** Versioning supports change monitoring, investigation, and downstream synchronization.

**Trade-off:** Retention, comparison, and storage policies become product concerns.

## 007 — Keep traces bounded

**Decision:** Record reconciliation decisions and contributing sources while capping trace size.

**Reason:** Engineers need enough evidence to reconstruct a decision without allowing unbounded operational records.

**Trade-off:** A bounded trace is intentionally not a byte-for-byte archive of every input.

## 008 — Keep the production source private

**Decision:** Publish architecture and engineering evidence as a case study while retaining application code privately.

**Reason:** The implementation includes proprietary product logic and sensitive operational detail.

**Trade-off:** Reviewers cannot compile the product from this repository, so public documentation must be precise about what was verified and what remains private.

