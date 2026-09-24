---
title: Google Cloud IAM
provider: gcp
category: security
---

Google Cloud IAM controls who (users, groups, service accounts) can do what (roles) on which
resources — the GCP equivalent of AWS IAM.

Best practices:
- Prefer predefined or custom roles scoped tightly over broad basic roles (Owner/Editor).
- Use service accounts for workloads, with keys avoided in favor of workload identity federation
  where possible.
- Enable MFA (2-Step Verification) for all human accounts, especially organization admins.
- Periodically audit IAM policies with Policy Analyzer / Recommender to remove unused grants.
