# Security and privacy

## Public repository boundary

This repository contains only public-safe documentation, a branded preview asset, and a validation script. It contains no production application source, prompts, credentials, customer data, database exports, logs, traces, internal hostnames, or deployment configuration.

The repository validation workflow checks for common credential/private-key patterns and rejects implementation file types that do not belong in this documentation-only showcase. That is a publication safeguard, not a substitute for product security review.

## Private product review

The private product repository contains authentication and authorization boundaries, scoped API keys, rate/usage controls, audit records, webhook signing mechanisms, health/readiness checks, observability integrations, incident runbooks, and a tracked security-audit process.

The existence of those mechanisms does not establish that every pathway is free of defects. Internal audit material includes remediation work, and this public case study intentionally avoids unsupported claims such as “fully secure,” “zero vulnerabilities,” or “compliant” without a named independent standard and current evidence.

## Data-handling principles represented by the design

- Preserve source attribution so a claim can be investigated.
- Separate customer and administrative interfaces and permissions.
- Treat retrieved web content as untrusted input.
- Keep secrets outside source-controlled public artifacts.
- Minimize what is copied from the private repository into public documentation.
- Avoid customer examples; use fictional demonstration data.
- Expose uncertainty instead of presenting weak evidence as certainty.

## Responsible disclosure

Do not post suspected product vulnerabilities, secrets, or customer information in a public GitHub issue. Use the product's private contact route at [lumensieve.com/contact](https://lumensieve.com/contact) and include only the minimum information needed to establish contact. Sensitive reproduction details should be exchanged through an agreed private channel.

## Scope of this repository's checks

The public validation workflow can detect missing documentation, broken relative links, selected secret patterns, and accidentally introduced implementation file types. It cannot audit the private product, verify production configuration, prove regulatory compliance, or guarantee that a credential will never be disclosed.

