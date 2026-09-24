---
title: AWS Auto Scaling
provider: aws
category: compute
---

AWS Auto Scaling automatically adjusts compute capacity up or down based on demand, using scaling
policies tied to metrics like CPU utilization or request count.

Benefits: cost optimization (you don't pay for idle capacity you provisioned "just in case"),
higher availability (unhealthy instances are replaced automatically), and better performance under
variable load.

Best practices:
- Set sensible minimum and maximum capacity bounds so scaling can't run away unexpectedly.
- Use target-tracking scaling policies for simplicity where possible.
- Combine with an Application Load Balancer to distribute traffic across the scaled fleet.
- Use health checks so unhealthy instances are replaced rather than left serving traffic.
