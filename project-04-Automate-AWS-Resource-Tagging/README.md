# Project: Automated AWS Resource Tagging & Compliance Enforcement

This project demonstrates how to **automate AWS resource tagging and enforce compliance** using **AWS native governance services**.  
The solution ensures that AWS resources always follow mandatory tagging standards without manual intervention.

The entire workflow is **event-driven and serverless**, designed to meet **industry-level cloud governance and cost management requirements**.

---

## Architecture Overview

The solution provisions and integrates the following components:

- **AWS Config** to continuously evaluate AWS resources for required tags
- A **custom AWS Config rule** backed by AWS Lambda
- **AWS Lambda (Python 3.12)** for compliance evaluation
- **Amazon EventBridge** to capture NON_COMPLIANT events
- A remediation **AWS Lambda function** to automatically apply missing tags
- **AWS IAM roles and policies** for secure service permissions
- **Amazon CloudWatch Logs** for monitoring and debugging

All resources are managed using AWS managed services, ensuring scalability, reliability, and minimal operational overhead.

This architecture follows AWS best practices for **governance, automation, and compliance**.

---

## Features

- Automated detection of missing or incorrect AWS resource tags
- Event-driven remediation using Amazon EventBridge
- Fully serverless and managed architecture
- Continuous compliance monitoring
- No manual tagging or remediation required
- Scalable across multiple AWS services and resources

---

## AWS Services Used

- AWS Config
- AWS Lambda (Python 3.12)
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch
- Amazon EC2 (for validation)

---

## Workflow

1. AWS resources are created or modified
2. AWS Config evaluates resources using a custom rule
3. Resources without mandatory tags are marked **NON_COMPLIANT**
4. AWS Config emits a compliance change event
5. Amazon EventBridge captures the event
6. Remediation Lambda function is triggered
7. Missing tags are automatically applied
8. Resource transitions back to **COMPLIANT** state

---

## Testing & Validation

- Created EC2 instances without required tags
- Verified **NON_COMPLIANT** status in AWS Config
- Confirmed EventBridge rule execution
- Checked Lambda execution logs in CloudWatch
- Validated automatic tag application
- Verified compliance status change to **COMPLIANT**

---

## Key Learnings

- Implementing cloud governance using AWS Config
- Writing custom compliance rules with Lambda
- Event-driven automation using Amazon EventBridge
- Automated remediation strategies
- AWS tagging best practices for cost and operations
- Designing production-ready AWS governance solutions

---

## Status

**Completed ✅**
