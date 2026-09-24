---
title: Multi-Cloud Strategy
provider: cross_cloud
category: operations
---

A multi-cloud strategy means intentionally using more than one cloud provider — as opposed to
"hybrid cloud" (mixing cloud with on-premises) or simply using a single provider.

Common reasons: avoiding vendor lock-in, using a specific provider's strength for a specific
workload (e.g. one provider's data/AI services), regulatory or data-residency requirements, and
negotiating leverage.

Trade-offs to weigh honestly:
- Operational complexity increases — teams need to understand multiple providers' equivalent
  services, IAM models, and networking.
- Consistent tooling (IaC, observability, CI/CD) across providers reduces but doesn't eliminate
  that complexity.
- Multi-cloud is not automatically "safer" or "cheaper" — it's a deliberate trade-off, best
  justified by a specific business or regulatory need rather than adopted by default.
