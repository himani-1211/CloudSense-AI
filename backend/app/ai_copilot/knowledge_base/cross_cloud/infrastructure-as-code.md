---
title: Infrastructure as Code (IaC)
provider: cross_cloud
category: operations
---

Infrastructure as Code means defining cloud resources in versioned, declarative configuration
files instead of clicking through consoles. Common tools include Terraform (multi-cloud),
AWS CloudFormation/CDK, Azure Bicep/ARM templates, and Google Cloud Deployment Manager.

Benefits: repeatable, reviewable (via pull requests) infrastructure changes, easier disaster
recovery (rebuild from code), and reduced configuration drift between environments.

Best practices:
- Store IaC in version control and require review before applying changes to production.
- Use remote state with locking (e.g. Terraform remote backends) to avoid concurrent-apply
  conflicts.
- Separate state and configuration per environment (dev/staging/prod) rather than one shared
  state file.
- Run a plan/diff step before every apply so changes are reviewed, not blind.
