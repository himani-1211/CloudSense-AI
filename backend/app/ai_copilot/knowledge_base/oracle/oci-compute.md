---
title: Oracle Cloud Infrastructure (OCI) Compute
provider: oracle
category: compute
---

OCI Compute is Oracle Cloud Infrastructure's virtual machine and bare-metal server offering — the
OCI equivalent of AWS EC2. Instances run in a compartment (OCI's resource-organization unit) and a
Virtual Cloud Network (VCN).

Best practices:
- Use compartments to isolate workloads and apply IAM policies at the compartment level.
- Use dynamic groups and instance principals instead of embedding credentials on instances.
- Restrict security list / network security group rules to required ports and sources.
- Use instance pools and autoscaling for workloads with variable demand.
