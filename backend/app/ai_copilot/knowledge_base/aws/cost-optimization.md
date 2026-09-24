---
title: AWS Cost Optimization
provider: aws
category: cost
---

Practical ways to reduce AWS spend without harming reliability:

- Right-size EC2 and RDS instances based on actual utilization rather than initial guesses.
- Stop or terminate idle EC2 instances, and delete unattached EBS volumes and old snapshots.
- Use S3 lifecycle policies to move cold data to cheaper storage classes.
- Use Savings Plans or Reserved Instances for steady-state, predictable workloads; use On-Demand
  or Spot for bursty or interruptible workloads.
- Tag resources consistently so cost can be attributed to teams, projects, or environments.
- Review AWS Cost Explorer / Trusted Advisor recommendations regularly rather than only reacting
  to a large bill at month end.
