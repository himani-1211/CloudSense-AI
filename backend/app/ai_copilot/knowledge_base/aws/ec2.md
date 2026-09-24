---
title: Amazon EC2 (Elastic Compute Cloud)
provider: aws
category: compute
---

Amazon EC2 (Elastic Compute Cloud) is AWS's virtual server service. It lets you launch and manage
virtual machines ("instances") in the cloud, choosing the CPU, memory, storage, and networking
capacity that fits your workload.

Common use cases: web hosting, APIs, backend applications, machine learning workloads, and
self-managed databases.

To launch an instance: open the EC2 console, click "Launch Instance", choose an Amazon Machine
Image (AMI), select an instance type, configure networking and storage, create or select a key
pair, review the configuration, and launch. After launch, connect using SSH (Linux) or RDP
(Windows).

Best practices:
- Use IAM roles instead of storing long-lived credentials on the instance.
- Enable CloudWatch monitoring for CPU, memory (via the agent), and disk metrics.
- Keep security groups restrictive — only open the ports you need, from the sources you trust.
- Stop or terminate unused instances to avoid paying for idle compute.
- Use Auto Scaling groups for workloads with variable demand.
- Patch AMIs regularly and rotate to updated images.
