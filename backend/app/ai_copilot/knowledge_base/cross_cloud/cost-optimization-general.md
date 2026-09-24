---
title: Cloud Cost Optimization (General Principles)
provider: cross_cloud
category: cost
---

Cost optimization principles that apply across AWS, Azure, GCP, and OCI:

- Eliminate waste first: idle compute, unattached storage volumes, and orphaned snapshots are the
  easiest savings with the lowest risk.
- Right-size before you commit: match instance/VM sizes to actual observed usage before buying
  reserved capacity or savings plans.
- Match commitment to predictability: use reserved/committed pricing for steady-state workloads,
  and on-demand or spot/preemptible pricing for bursty or interruptible ones.
- Use storage tiering: move data that's rarely accessed to cheaper "cold" storage tiers instead of
  leaving everything on the most expensive tier.
- Tag and attribute cost: consistent tagging lets you see which team, project, or environment is
  driving spend, which is a prerequisite for optimizing it.
- Review regularly: cost optimization isn't a one-time project — usage patterns change, so
  recommendations should be revisited periodically.
