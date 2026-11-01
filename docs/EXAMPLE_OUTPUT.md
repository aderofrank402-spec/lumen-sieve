# Sanitized output example

The example below is fictional. It demonstrates concepts verified in the private protocol contracts and reconciliation implementation; it is not copied from a customer record and is not a promise that every API endpoint returns this exact JSON envelope.

```json
{
  "profile_id": "profile_demo_001",
  "query": {
    "name": "Northstar Components",
    "domain": "northstar.example"
  },
  "status": "complete",
  "fields": {
    "legal_name": {
      "value": "Northstar Components Ltd",
      "confidence": 0.92,
      "reconciliation_method": "consensus",
      "attributions": [
        {
          "source_url": "https://northstar.example/about",
          "source_type": "official_website"
        },
        {
          "source_url": "https://registry.example/companies/northstar-components",
          "source_type": "business_registry"
        }
      ]
    },
    "headquarters": {
      "value": "Nairobi, Kenya",
      "confidence": 0.78,
      "reconciliation_method": "field_rule",
      "attributions": [
        {
          "source_url": "https://northstar.example/contact",
          "source_type": "official_website"
        }
      ]
    },
    "employee_count": {
      "value": null,
      "confidence": 0.0,
      "reconciliation_method": "no_evidence",
      "attributions": []
    }
  }
}
```

## How to read it

- `value` is the selected field value, not a detached claim.
- `confidence` is bounded to the range represented by the service contract and is intended as a decision signal, not a guarantee.
- `reconciliation_method` explains how the field reached its state.
- `attributions` identify the sources that contributed to the result.
- `no_evidence` preserves missing knowledge instead of replacing it with a guess.

