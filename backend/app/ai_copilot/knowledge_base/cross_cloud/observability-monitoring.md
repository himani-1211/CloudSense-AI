---
title: Observability and Monitoring
provider: cross_cloud
category: observability
---

Observability is the ability to understand a system's internal state from its external outputs —
metrics, logs, and traces. It's what lets an engineer answer "what's wrong?" instead of just "is
something wrong?".

- Metrics: numeric time-series data (CPU, latency, error rate, queue depth) good for alerting and
  trends.
- Logs: discrete, timestamped events, good for root-cause investigation.
- Traces: track a single request as it flows across services, good for diagnosing latency in
  distributed systems.

Best practices:
- Alert on symptoms that affect users (latency, error rate, availability), not just raw resource
  metrics.
- Avoid alert fatigue — every alert should be actionable, or it should not page anyone.
- Centralize logs so engineers aren't hunting across a dozen different consoles during an
  incident.
- Set retention based on actual need (compliance, debugging window) rather than keeping everything
  forever by default.
