---
title: Amazon CloudWatch
provider: aws
category: observability
---

Amazon CloudWatch is AWS's monitoring and observability service. It collects metrics, logs, and
events from AWS resources and applications, and can trigger alarms and automated actions.

Common uses: tracking CPU/memory/disk metrics, aggregating application logs, setting alarms that
notify via SNS or trigger Auto Scaling, and building operational dashboards.

Best practices:
- Set alarms on the metrics that actually predict user-facing problems (latency, error rate,
  saturation), not just raw CPU.
- Centralize logs from EC2, Lambda, and containers into CloudWatch Logs for easier troubleshooting.
- Use dashboards to give teams a shared, at-a-glance view of system health.
- Set log retention policies — logs kept forever have an ongoing storage cost.
