---
title: AWS Lambda
provider: aws
category: serverless
---

AWS Lambda is a serverless compute service. You upload code and AWS automatically runs it in
response to events — you never provision or manage servers, and you pay only for compute time
consumed.

Common use cases: APIs (often behind API Gateway), file processing (e.g. triggered by S3
uploads), scheduled jobs (via EventBridge), and event-driven or streaming applications.

To create a function: open AWS Lambda, click "Create function", choose "Author from scratch",
select a runtime, write or upload your code, configure triggers, and deploy.

Best practices:
- Keep functions small and single-purpose; use one function per responsibility.
- Set an appropriate memory/timeout — memory also scales available CPU.
- Use environment variables (and Secrets Manager/SSM for secrets) instead of hardcoding config.
- Watch for cold starts in latency-sensitive paths; consider provisioned concurrency if needed.
- Grant the function's execution role only the permissions it actually needs.
