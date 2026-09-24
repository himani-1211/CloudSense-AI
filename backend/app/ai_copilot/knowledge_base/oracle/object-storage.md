---
title: OCI Object Storage
provider: oracle
category: storage
---

OCI Object Storage is Oracle Cloud Infrastructure's object storage service — the OCI equivalent of
AWS S3 — with Standard and Archive storage tiers.

Best practices:
- Keep buckets private by default and grant access via IAM policies scoped to the bucket.
- Use lifecycle policies to move older objects to the Archive tier or delete them.
- Enable versioning for buckets holding critical data.
- Use pre-authenticated requests for temporary, scoped access instead of making a bucket public.
