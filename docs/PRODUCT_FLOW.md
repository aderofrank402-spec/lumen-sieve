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
flowchart TD
    A[Field evidence rows] --> B[Validate identity and evidence shape]
    B --> C[Apply source credibility]
    C --> D[Apply freshness and extraction confidence]
    D --> E[Group equivalent candidate values]
    E --> F{Field rule resolves conflict?}
    F -->|yes| G[Rule-backed verdict]
    F -->|no| H{Consensus is sufficient?}
    H -->|yes| I[Consensus verdict]
    H -->|no| J{Bounded arbitration available?}
    J -->|yes| K[Arbitrated verdict or rejection]
    J -->|no| L[Unresolved conflict]
    G --> M[Calibrate confidence and attach sources]
    I --> M
    K --> M
    L --> N[Explicit unresolved result]
    M --> O[Validate and emit bounded trace]
```

## Change monitoring

1. A customer creates a monitor for a resolved profile and selects a confidence threshold or notification behavior.
2. A scheduled refresh produces a new profile version.
3. Field-level changes are compared against the previous version.
4. Eligible changes are displayed in the dashboard and can enter notification or webhook delivery flows.
5. Delivery attempts and operational failures remain observable for retry and support workflows.

## Failure behavior

The pipeline can distinguish failures by stage rather than returning one generic error. Examples represented in the implementation include unavailable sources, fetch failures, extraction failures, no evidence, unresolved conflicts, quota/rate rejection, and downstream delivery failure. A failed source does not automatically imply that every independent source or the complete lookup must fail.

