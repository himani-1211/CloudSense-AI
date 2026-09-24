---
title: Kubernetes
provider: cross_cloud
category: containers
---

Kubernetes (K8s) is a container orchestration platform. It manages deployment, scaling,
networking, load balancing, and self-healing for containerized applications, and runs the same way
on AWS (EKS), Azure (AKS), Google Cloud (GKE), or on-premises.

Best practices:
- Set resource requests/limits on every pod so the scheduler can place workloads sensibly and
  avoid noisy-neighbor issues.
- Use namespaces to separate environments or teams within a cluster.
- Use readiness and liveness probes so unhealthy pods are restarted or removed from load-balancing
  automatically.
- Apply the principle of least privilege to service accounts and RBAC roles.
- Keep the cluster and node images patched to current supported versions.
