# Project: Self-Healing EC2 Infrastructure using CloudWatch Recovery

This project demonstrates how to implement a **self-healing infrastructure pattern on AWS** using Amazon CloudWatch alarms and EC2 recovery actions.

The system automatically detects infrastructure failures and recovers the EC2 instance without manual intervention.

This approach improves reliability, reduces downtime, and is widely used in production environments.

---

## Architecture Overview

The solution integrates the following AWS services:

- Amazon EC2 (Test instance)
- Amazon CloudWatch (Monitoring & alarms)
- EC2 Recovery Action (Automated recovery)

Architecture workflow:

EC2 Instance  
↓  
CloudWatch monitors **StatusCheckFailed_System**  
↓  
CloudWatch Alarm triggers when system failure detected  
↓  
EC2 Recovery Action executes  
↓  
Instance automatically moved to healthy hardware

---

## Features

- Automated infrastructure recovery
- Hardware failure detection
- No manual intervention required
- Built using AWS native monitoring
- Production-style reliability pattern

---

## AWS Services Used

- Amazon EC2
- Amazon CloudWatch

---

## Workflow

1. Launch an EC2 instance.
2. Configure CloudWatch to monitor the metric:

   StatusCheckFailed_System

3. Create a CloudWatch alarm with condition:

   StatusCheckFailed_System ≥ 1

4. Configure the alarm action:

   Recover this instance

5. If AWS detects hardware or system failure:

   CloudWatch Alarm → EC2 Recovery Action → Instance recovered.

---

## Testing & Validation

The following steps were used to verify the setup:

- Created EC2 instance for monitoring
- Configured CloudWatch alarm
- Enabled EC2 recovery action
- Verified alarm creation
- Confirmed monitoring metrics in EC2 console

Screenshots demonstrating the workflow are included in this repository.

---

## Key Learnings

- Infrastructure resilience patterns
- CloudWatch monitoring configuration
- Automated EC2 recovery mechanisms
- Designing self-healing infrastructure
- Reliability engineering fundamentals

---

## Status

Completed ✅
