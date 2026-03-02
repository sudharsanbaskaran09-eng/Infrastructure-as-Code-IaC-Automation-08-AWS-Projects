# Project: Automated EC2 OS Patching using AWS Systems Manager (SSM)

This project demonstrates how to automate operating system patch management for Amazon EC2 instances using AWS Systems Manager Patch Manager.

The solution ensures that EC2 instances remain secure, compliant, and up-to-date without manual SSH-based patching.

The entire workflow is managed, scalable, and production-ready, aligned with industry-level cloud security and infrastructure governance standards.

---

## Architecture Overview

The solution provisions and integrates the following components:

- Amazon EC2 (Amazon Linux 2023) as the managed server
- AWS Systems Manager (SSM) for centralized instance management
- SSM Agent for secure remote communication
- AWS-managed Patch Baseline for approved patch policies
- Patch Scan & Install operations using Patch Manager
- Compliance Reporting Dashboard for visibility
- AWS IAM role (AmazonSSMManagedInstanceCore) for secure service permissions

All operations are performed using AWS managed services, ensuring:

- No direct SSH dependency
- Secure remote management
- Scalable patch lifecycle automation
- Centralized compliance tracking

This architecture follows AWS best practices for security hardening, automation, and operational excellence.

---

## Features

- Automated patch scanning for EC2 instances
- Patch installation without manual intervention
- Centralized compliance visibility
- No SSH-based maintenance required
- Secure IAM-based instance management
- Enterprise-style patch lifecycle workflow
- Scalable for multiple EC2 instances

---

## AWS Services Used

- AWS Systems Manager (Patch Manager)
- Amazon EC2
- AWS IAM
- SSM Agent
- Patch Baselines
- Compliance Reporting

---

## Workflow

1. EC2 instance is launched with SSM IAM role attached  
2. Instance registers automatically as a Managed Node in Systems Manager  
3. AWS-managed Patch Baseline defines approved updates  
4. Patch Scan is executed to detect missing updates  
5. Patch Install operation applies required updates  
6. Compliance Reporting verifies patch status  
7. Instance reaches COMPLIANT state  

---

## Testing & Validation

- Verified EC2 registration in Systems Manager
- Executed Patch Scan operation successfully
- Executed Patch Install operation
- Confirmed zero missing patches
- Validated compliance status as COMPLIANT
- Confirmed no failed patch installations

All screenshots and proof of execution are available in this repository.

---

## Key Learnings

- Centralized patch management using AWS Systems Manager
- Automating OS updates without SSH access
- Understanding patch baselines and compliance reporting
- Implementing secure IAM-based remote management
- Designing production-ready patch lifecycle automation
- Improving infrastructure security posture

---

## Security Impact

Automated patching reduces:

- Vulnerability exposure window
- Human error in manual updates
- Configuration drift
- Operational overhead

It improves:

- Compliance readiness
- Infrastructure reliability
- Security governance maturity

---

## Status

Completed ✅

Compliance Status: 100%  
Missing Patches: 0  
Failed Installations: 0  
Environment: Amazon Linux 2023  
Management: AWS Systems Manager Patch Manager  
