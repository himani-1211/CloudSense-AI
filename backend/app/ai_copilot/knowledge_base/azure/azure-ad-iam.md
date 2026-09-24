---
title: Microsoft Entra ID (Azure AD) and IAM
provider: azure
category: security
---

Microsoft Entra ID (formerly Azure Active Directory) is Azure's identity and access management
service — the Azure equivalent of AWS IAM, plus full identity/directory services.

Best practices:
- Use role-based access control (RBAC) scoped to the narrowest resource group or resource needed.
- Prefer Managed Identities over storing credentials in application config for Azure-hosted
  workloads.
- Require MFA for all users, especially those with elevated (Owner/Contributor) roles.
- Regularly review role assignments and remove unused accounts or stale permissions via Access
  Reviews.
