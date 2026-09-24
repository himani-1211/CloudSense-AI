---
title: Google Cloud Functions
provider: gcp
category: serverless
---

Google Cloud Functions (and Cloud Run for containerized workloads) are Google Cloud's serverless
compute offerings — the GCP equivalent of AWS Lambda. Code runs in response to HTTP requests or
events (Pub/Sub, Storage, Firestore) without managing servers.

Best practices:
- Keep functions single-purpose and stateless.
- Use Secret Manager for credentials instead of hardcoding them in source or environment
  variables.
- Set appropriate memory and timeout values based on actual workload profiling.
- Scope the function's service account to the minimum permissions it needs.
