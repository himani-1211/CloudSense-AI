---
title: Amazon EBS (Elastic Block Store)
provider: aws
category: storage
---

Amazon EBS provides persistent block storage volumes for use with EC2 instances, similar to a
virtual hard disk. Volumes persist independently of the instance lifecycle (unless explicitly
deleted).

Best practices:
- Take regular EBS snapshots for backup and disaster recovery.
- Delete unattached volumes — they still incur cost even when not attached to a running instance.
- Choose the right volume type (gp3 for general purpose, io2 for high-IOPS workloads, st1/sc1 for
  throughput-oriented workloads) instead of defaulting to the most expensive option.
- Enable encryption at rest for volumes containing sensitive data.
