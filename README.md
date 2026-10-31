# LUMEN Sieve

Evidence-first company intelligence for turning a business name or domain into a cited, reconciled profile with confidence signals.

[Live product](https://lumensieve.com) · API-first · source-aware · built for production workflows

> The production source code is private. This repository is a public engineering case study and contains no application code, credentials, prompts, customer data, or deployment configuration.

## The problem

Company data is fragmented, stale, and frequently contradictory. A single provider response may look complete while hiding weak provenance or unresolved conflicts. LUMEN Sieve is designed to discover independent sources, reconcile competing claims, preserve citations, and make uncertainty visible to downstream systems and people.

## Product surface

- Company and domain resolution through a dashboard and API
- Source discovery, page verification, crawling, and profile assembly
- Field-level citations and confidence signals
- Reconciliation of conflicting evidence instead of silent overwrites
- Webhook-oriented integration for asynchronous workflows
- Monitoring and operational tracing for long-running resolution jobs

## High-level architecture

```text
Dashboard / API client
          │
      API gateway
          │
  resolution orchestration
    ┌─────┼──────────┐
 discovery  crawling  provider adapters
    └─────┼──────────┘
  evidence reconciliation
          │
 cited profile + confidence
          │
 API response / webhook / monitoring
```

The production system combines Go services, Python intelligence and discovery services, a Next.js interface, PostgreSQL, Redis, search/analytics storage, gRPC, containers, and distributed tracing.

## Engineering priorities

- **Provenance:** retain where each claim came from.
- **Corroboration:** distinguish repeated copies from genuinely independent support.
- **Uncertainty:** expose conflict and confidence rather than invent certainty.
- **Resilience:** isolate providers and degrade deliberately when a source is unavailable.
- **Observability:** trace discovery, crawling, and synthesis as separate stages.
- **Safety:** keep credentials and private product logic outside public artifacts.

## My role

I designed and built LUMEN Sieve as an end-to-end product spanning backend services, intelligence workflows, API contracts, data modeling, deployment, and production operations.

## Source availability

The implementation remains in a private repository because it contains proprietary resolution and reconciliation logic. I can discuss architecture and trade-offs in an interview without disclosing private source.
