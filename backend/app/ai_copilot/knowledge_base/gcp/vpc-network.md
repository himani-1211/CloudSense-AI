---
title: Google Cloud VPC
provider: gcp
category: networking
---

Google Cloud VPC is the GCP equivalent of AWS VPC / Azure VNet — a global, software-defined
network for your GCP resources, with subnets, firewall rules, and routes.

Best practices:
- Use firewall rules scoped to specific tags/service accounts rather than broad IP ranges.
- Keep databases and internal services without external IPs; use Cloud NAT for outbound-only
  internet access.
- Separate environments (dev/staging/prod) into different VPCs or projects.
- Enable VPC Flow Logs when you need traffic visibility for troubleshooting or audits.
