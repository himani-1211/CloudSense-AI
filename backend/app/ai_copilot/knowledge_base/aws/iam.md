---
title: AWS IAM (Identity and Access Management)
provider: aws
category: security
---

AWS IAM manages authentication and authorization across an AWS account: users, groups, roles, and
policies.

Best practices:
- Follow the principle of least privilege — grant only the permissions a user or service actually
  needs.
- Prefer IAM roles over long-lived access keys, especially for workloads running on EC2, Lambda,
  or ECS.
- Enable MFA for all human users, especially anyone with administrative access.
- Avoid using the root account for day-to-day work; create individual IAM users or use IAM
  Identity Center.
- Regularly review and remove unused users, roles, and access keys with IAM Access Analyzer or
  credential reports.
