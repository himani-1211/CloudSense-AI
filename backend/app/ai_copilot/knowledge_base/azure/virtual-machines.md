---
title: Azure Virtual Machines
provider: azure
category: compute
---

Azure Virtual Machines (VMs) are Microsoft Azure's on-demand, scalable virtual server offering —
the Azure equivalent of AWS EC2. You choose an image, a VM size (CPU/memory/disk profile), and
networking, and Azure provisions the virtual machine.

Common use cases: web hosting, custom applications, dev/test environments, and lift-and-shift
migrations from on-premises servers.

Best practices:
- Use Managed Identities instead of embedding credentials on the VM.
- Enable Azure Monitor / diagnostics for CPU, memory, and disk metrics.
- Restrict inbound access with Network Security Groups (NSGs); avoid open RDP/SSH to the internet.
- Use Virtual Machine Scale Sets for workloads with variable demand.
- Deallocate (not just stop) unused VMs to avoid paying for reserved compute.
