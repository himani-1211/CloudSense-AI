---
title: Google Compute Engine
provider: gcp
category: compute
---

Google Compute Engine (GCE) is Google Cloud's virtual machine service — the GCP equivalent of AWS
EC2. You choose a machine type, image, and network configuration to launch a VM instance.

Common use cases: web hosting, custom applications, batch processing, and lift-and-shift
migrations.

Best practices:
- Use service accounts with narrowly scoped IAM roles instead of default broad-permission
  accounts.
- Use instance templates and Managed Instance Groups for scaling and self-healing.
- Enable OS Login and firewall rules that restrict SSH access rather than allowing it from
  anywhere.
- Stop or delete unused instances; persistent disks on stopped instances still incur cost.
