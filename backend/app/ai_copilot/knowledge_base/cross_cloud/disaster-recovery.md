---
title: Disaster Recovery and Backup Strategy
provider: cross_cloud
category: reliability
---

Disaster recovery (DR) planning centers on two key metrics:

- RTO (Recovery Time Objective): how long the system can be down before it's unacceptable.
- RPO (Recovery Point Objective): how much data loss (measured in time) is acceptable.

Common DR strategies, roughly in increasing cost and decreasing recovery time:
- Backup and restore: cheapest, slowest recovery.
- Pilot light: minimal version of the environment always running, scaled up during a disaster.
- Warm standby: a scaled-down but fully functional copy running in another region.
- Multi-site active/active: full redundancy across regions with near-zero downtime, most
  expensive.

Best practices:
- Test restores, not just backups — an untested backup is not a verified recovery plan.
- Choose a DR strategy based on actual business RTO/RPO requirements, not the most impressive
  architecture.
- Document and rehearse the failover process so it doesn't rely on tribal knowledge during an
  actual incident.
