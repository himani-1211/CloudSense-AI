---
title: Amazon VPC (Virtual Private Cloud)
provider: aws
category: networking
---

Amazon VPC lets you create an isolated virtual network inside AWS, with full control over IP
addressing, subnets, route tables, gateways, and network security.

Key building blocks:
- Subnets: public (route to an internet gateway) and private (no direct internet route).
- Route tables: control where traffic from a subnet is sent.
- Security groups: stateful, instance-level firewalls.
- Network ACLs: stateless, subnet-level firewalls.
- NAT gateways: let private-subnet resources reach the internet outbound without being reachable
  from it.

Best practices:
- Place databases and internal services in private subnets.
- Use separate VPCs (or well-segmented subnets) per environment (dev/staging/prod).
- Keep security group rules as narrow as possible — avoid 0.0.0.0/0 on sensitive ports.
- Use VPC Flow Logs when you need visibility into network traffic for troubleshooting or audits.
