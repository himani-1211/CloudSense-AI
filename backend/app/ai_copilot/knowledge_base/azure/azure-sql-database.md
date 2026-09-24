---
title: Azure SQL Database
provider: azure
category: database
---

Azure SQL Database is Microsoft Azure's managed relational database service — broadly the Azure
equivalent of AWS RDS. It handles patching, backups, and high availability for SQL Server-compatible
workloads.

Best practices:
- Enable geo-replication or zone redundancy for production workloads needing high availability.
- Use automated backups and periodically test point-in-time restore.
- Enforce TLS for connections and enable Transparent Data Encryption (TDE) at rest.
- Right-size the service tier (DTU or vCore model) based on actual usage rather than guessing.
- Restrict access with firewall rules and private endpoints instead of allowing broad public
  access.
