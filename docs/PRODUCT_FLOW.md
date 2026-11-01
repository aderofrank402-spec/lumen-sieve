# Product flow

This lifecycle is derived from implemented routes, protocol events, services, and UI states in the private repository.

## Interactive lookup

```mermaid
sequenceDiagram
    actor User
    participant UI as Dashboard
    participant API as API gateway
    participant P as Profile orchestration
    participant D as Discovery
    participant F as Fetch pool
    participant E as Extraction
    participant R as Reconciliation
    participant DB as Profile store

    User->>UI: Submit company name or domain
    UI->>API: Authenticated lookup request
    API->>API: Validate scope, input, quota, idempotency
    API->>P: Start or reuse resolution
    P->>D: Discover candidate sources
    D-->>P: Candidate URLs and identity signals
    P->>F: Fetch selected sources
    F-->>P: Content or typed failure
    P->>E: Extract structured field evidence
    E-->>P: Values, confidence, source context
    P->>R: Reconcile evidence by field
    R-->>P: Value, confidence, method, attribution
    P->>DB: Store versioned profile and trace metadata
    P-->>API: Resolution result
    API-->>UI: Profile or progress response
    UI-->>User: Cited company profile
```

## Field reconciliation

```mermaid
graph TD
    evidence["Field evidence rows"] --> validate["Validate identity and evidence shape"]
    validate --> credibility["Apply source credibility"]
    credibility --> freshness["Apply freshness and extraction confidence"]
    freshness --> group["Group equivalent candidate values"]
    group --> rules{"Field rule resolves conflict?"}
    rules -->|"Yes"| ruleverdict["Rule-backed verdict"]
    rules -->|"No"| consensus{"Consensus is sufficient?"}
    consensus -->|"Yes"| consensusverdict["Consensus verdict"]
    consensus -->|"No"| arbitration{"Bounded arbitration available?"}
    arbitration -->|"Yes"| arbitrated["Arbitrated verdict or rejection"]
    arbitration -->|"No"| unresolved["Unresolved conflict"]
    ruleverdict --> confidence["Calibrate confidence and attach sources"]
    consensusverdict --> confidence
    arbitrated --> confidence
    unresolved --> explicit["Explicit unresolved result"]
    confidence --> trace["Validate and emit bounded trace"]
```

## Change monitoring

1. A customer creates a monitor for a resolved profile and selects a confidence threshold or notification behavior.
2. A scheduled refresh produces a new profile version.
3. Field-level changes are compared against the previous version.
4. Eligible changes are displayed in the dashboard and can enter notification or webhook delivery flows.
5. Delivery attempts and operational failures remain observable for retry and support workflows.

## Failure behavior

The pipeline can distinguish failures by stage rather than returning one generic error. Examples represented in the implementation include unavailable sources, fetch failures, extraction failures, no evidence, unresolved conflicts, quota/rate rejection, and downstream delivery failure. A failed source does not automatically imply that every independent source or the complete lookup must fail.

