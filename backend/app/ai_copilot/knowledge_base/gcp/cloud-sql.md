---
title: Google Cloud SQL
provider: gcp
category: database
---

Google Cloud SQL is Google Cloud's managed relational database service — the GCP equivalent of AWS
RDS — supporting MySQL, PostgreSQL, and SQL Server.

Best practices:
- Enable high-availability (regional) configuration for production instances.
- Turn on automated backups and point-in-time recovery.
- Require SSL/TLS connections and avoid assigning a public IP unless necessary; prefer private IP
  or the Cloud SQL Auth Proxy.
- Right-size machine type and storage based on observed usage rather than initial guesses.
