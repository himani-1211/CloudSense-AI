---
title: Oracle Autonomous Database
provider: oracle
category: database
---

Oracle Autonomous Database is OCI's self-managing relational database service — broadly the OCI
equivalent of AWS RDS/Aurora — with automated patching, tuning, scaling, and backups.

Best practices:
- Use the built-in automated backups and test restores periodically.
- Scope database access through OCI IAM and database-level users with least privilege.
- Enable network access control lists (ACLs) or private endpoints instead of leaving the database
  open to the public internet.
- Use auto-scaling for OCPU/storage rather than statically over-provisioning for peak load.
