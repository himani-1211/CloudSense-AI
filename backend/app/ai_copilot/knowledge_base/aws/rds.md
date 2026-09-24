---
title: Amazon RDS (Relational Database Service)
provider: aws
category: database
---

Amazon RDS is AWS's managed relational database service. It handles provisioning, patching,
backups, and failover for you, across engines including PostgreSQL, MySQL, MariaDB, SQL Server,
and Oracle.

Best practices:
- Enable Multi-AZ deployments for production workloads to get automatic failover.
- Turn on automated backups and test restores periodically.
- Use read replicas to offload read-heavy traffic from the primary instance.
- Encrypt storage at rest and require TLS for connections.
- Right-size instance classes based on actual CPU/memory/IOPS usage instead of guessing.
- Restrict network access via security groups; avoid making databases publicly accessible.
