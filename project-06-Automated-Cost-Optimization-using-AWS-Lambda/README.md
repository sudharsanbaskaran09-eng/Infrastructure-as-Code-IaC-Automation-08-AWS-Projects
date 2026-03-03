# Project: Automated EC2 Cost Optimization using AWS Lambda & EventBridge

This project demonstrates how to automate EC2 cost optimization using a serverless, event-driven architecture.

The solution detects idle EC2 instances based on CPU utilization and automatically stops them, reducing unnecessary cloud spending.

The workflow is production-style and includes guardrails to prevent accidental shutdown of critical infrastructure.

---

## Architecture Overview

The solution provisions and integrates the following components:

- Amazon EC2 (Test Instance)
- AWS Lambda (Python 3.12)
- Amazon EventBridge (Scheduled Trigger)
- Amazon CloudWatch (CPU Metrics Monitoring)
- AWS IAM Role for secure permissions

The architecture follows a data-driven automation model:

EventBridge → Lambda → CloudWatch Metrics → EC2 Stop Action

This ensures fully automated and controlled cost optimization.

---

## Features

- Automated detection of idle EC2 instances
- CPU-based decision engine (data-driven automation)
- Tag-based safeguard (AutoStop = true)
- Scheduled execution every 5 minutes
- Serverless architecture (no infrastructure to manage)
- Production-safe shutdown logic

---

## AWS Services Used

- AWS Lambda
- Amazon EC2
- Amazon CloudWatch
- Amazon EventBridge
- AWS IAM

---

## Workflow

1. EC2 instance is launched with tag:
   AutoStop = true

2. Amazon EventBridge triggers Lambda every 5 minutes

3. Lambda:
   - Checks running EC2 instances
   - Validates AutoStop tag
   - Fetches CPU metrics from CloudWatch
   - Calculates average CPU utilization (last 10 minutes)

4. If:
   CPU < 5%
   AND AutoStop = true
   AND Instance state = running

5. Lambda stops the EC2 instance

6. CloudWatch Logs capture execution details

---

## Testing & Validation

- Launched EC2 instance with AutoStop tag
- Verified Lambda execution via CloudWatch Logs
- Confirmed CPU utilization below threshold
- Verified automatic EC2 stop action
- Confirmed EventBridge scheduled execution

All screenshots, architecture diagram, Lambda code, and execution logs are included in this repository.

---

## Key Learnings

- Event-driven serverless automation
- CloudWatch metric integration
- Automated cost control strategies
- Safe infrastructure guardrails
- IAM-based permission design
- Real-world FinOps implementation

---

## Security & Cost Impact

This automation reduces:

- Idle infrastructure costs
- Manual monitoring overhead
- Risk of forgotten test instances
- Operational inefficiencies

It improves:

- Cloud governance
- Financial accountability
- Infrastructure discipline
- Automation maturity

---

## Status

Completed ✅

Automation Type: Scheduled (Every 5 minutes)
Decision Logic: CPU < 5% + AutoStop tag validation
Environment: Amazon Linux EC2
Architecture: Serverless Event-Driven
