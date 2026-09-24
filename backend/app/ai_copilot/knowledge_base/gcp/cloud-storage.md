---
title: Google Cloud Storage
provider: gcp
category: storage
---

Google Cloud Storage (GCS) is Google Cloud's object storage service — the GCP equivalent of AWS
S3. Objects are stored in globally namespaced buckets with configurable storage classes (Standard,
Nearline, Coldline, Archive).

Best practices:
- Keep buckets private by default; grant access via IAM rather than making buckets publicly
  readable unless intentional (e.g. static site hosting).
- Use lifecycle rules to transition old objects to cheaper storage classes or delete them.
- Enable versioning on buckets holding important data.
- Use uniform bucket-level access (IAM only) instead of mixing ACLs and IAM where possible, for
  simpler and more auditable permissions.
