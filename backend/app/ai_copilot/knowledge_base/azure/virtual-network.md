---
title: Azure Virtual Network (VNet)
provider: azure
category: networking
---

Azure Virtual Network (VNet) is the Azure equivalent of AWS VPC — an isolated network for your
Azure resources, with control over address spaces, subnets, and routing.

Key building blocks: subnets, Network Security Groups (NSGs, similar to security groups), route
tables, and NAT gateways for outbound-only internet access from private subnets.

Best practices:
- Segment workloads into subnets by tier (web, app, data) and apply NSGs per subnet.
- Avoid exposing management ports (RDP/SSH) directly to the internet — use Azure Bastion or a VPN.
- Use separate VNets or well-segmented subnets per environment.
- Enable NSG flow logs when you need visibility into traffic for troubleshooting or audits.
