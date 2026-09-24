---
title: Azure Functions
provider: azure
category: serverless
---

Azure Functions is Microsoft Azure's serverless compute offering — the Azure equivalent of AWS
Lambda. You deploy code that runs in response to triggers (HTTP requests, queue messages, timers,
blob events) and pay only for execution time.

Best practices:
- Keep functions small and focused on a single responsibility.
- Use Application Settings / Key Vault references for configuration and secrets instead of
  hardcoding them.
- Watch cold-start latency on the Consumption plan; use Premium plan for latency-sensitive
  workloads.
- Scope the function's managed identity permissions narrowly.
