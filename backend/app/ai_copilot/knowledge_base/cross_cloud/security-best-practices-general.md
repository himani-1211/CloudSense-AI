---
title: Cloud Security Best Practices (General Principles)
provider: cross_cloud
category: security
---

Security principles that apply across cloud providers:

- Least privilege: every identity (human or service) should have only the permissions it needs,
  nothing more.
- Defense in depth: don't rely on a single control (e.g. a firewall rule) — layer network,
  identity, and data-level protections.
- Encrypt data at rest and in transit by default.
- Require MFA for human accounts, especially anyone with administrative access.
- Keep an audit trail: enable activity logging (CloudTrail, Azure Activity Log, GCP Audit Logs) so
  you can reconstruct what happened after an incident.
- Patch and update regularly rather than treating patching as optional maintenance.
- Avoid exposing management interfaces (SSH/RDP, admin consoles) directly to the public internet.
