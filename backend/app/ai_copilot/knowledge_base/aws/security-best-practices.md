---
title: AWS Security Best Practices
provider: aws
category: security
---

Baseline security practices for an AWS account:

- Enable MFA on the root account and all privileged IAM users; avoid using the root account
  day-to-day.
- Follow least privilege for IAM roles and policies; avoid wildcard ("*") permissions in
  production.
- Keep S3 buckets private by default; only make specific buckets public intentionally.
- Encrypt data at rest (S3, EBS, RDS) and in transit (TLS).
- Restrict security group rules to known IP ranges and required ports; avoid open SSH/RDP to
  0.0.0.0/0.
- Enable AWS CloudTrail to keep an audit log of account activity.
- Use AWS Config or Security Hub to continuously check for drift from your security baseline.
