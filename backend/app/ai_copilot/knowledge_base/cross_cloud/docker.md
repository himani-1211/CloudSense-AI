---
title: Docker and Containerization
provider: cross_cloud
category: containers
---

Docker is a containerization platform. Containers package an application together with its
dependencies into a single portable unit, so it runs consistently across environments — from a
developer's laptop to any cloud provider.

Benefits: lightweight compared to full VMs, portable across environments, fast to start, and easy
to scale horizontally.

Best practices:
- Keep images small (use slim/minimal base images) to reduce attack surface and speed up
  deployments.
- Never run containers as root in production unless required.
- Pin base image versions rather than using `latest`, for reproducible builds.
- Scan images for known vulnerabilities before deploying.
