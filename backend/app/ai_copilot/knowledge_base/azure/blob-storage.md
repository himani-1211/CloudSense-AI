---
title: Azure Blob Storage
provider: azure
category: storage
---

Azure Blob Storage is Microsoft Azure's object storage service — the Azure equivalent of AWS S3.
Data is stored as blobs inside containers within a storage account.

Common use cases: unstructured data storage, static website hosting, backups, and data lakes
(via Azure Data Lake Storage Gen2 on top of Blob Storage).

Best practices:
- Keep containers private by default; only make specific containers public intentionally.
- Use lifecycle management policies to move cool/rarely-accessed data to cooler access tiers
  (Cool, Archive) to reduce cost.
- Enable soft delete and versioning to protect against accidental deletion.
- Use Azure AD-based access (RBAC/SAS with limited scope) rather than broadly shared account keys.
