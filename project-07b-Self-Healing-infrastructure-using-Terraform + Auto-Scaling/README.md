# Project: Self-Healing Infrastructure using Terraform & AWS Auto Scaling

This project demonstrates how to build a **self-healing cloud infrastructure** using **Terraform and AWS native scaling services**.

The infrastructure automatically detects unhealthy EC2 instances and **replaces them with new instances without manual intervention**, ensuring high availability and reliability.

The entire infrastructure is deployed using **Infrastructure as Code (IaC)**, making it fully automated, repeatable, and production-ready.

---

## Architecture Overview

The solution provisions and integrates the following components:

- **Terraform** to define and provision infrastructure as code
- **AWS EC2 Launch Template** to define instance configuration
- **AWS Auto Scaling Group** to automatically maintain instance health
- **Amazon EC2 instances** for compute resources
- **AWS VPC default subnet** for network placement

The Auto Scaling Group continuously monitors instance health.  
If an EC2 instance fails a health check or is terminated, the Auto Scaling Group **automatically launches a replacement instance**.

This architecture follows AWS best practices for **high availability, resilience, and infrastructure automation**.

---

## Features

- Fully automated infrastructure provisioning using Terraform
- Self-healing EC2 infrastructure
- Automatic instance replacement on failure
- Infrastructure lifecycle management
- Highly available architecture design
- Production-style cloud infrastructure deployment

---

## AWS Services Used

- AWS EC2
- AWS EC2 Launch Templates
- AWS Auto Scaling
- AWS VPC

---

## Workflow

1. Terraform defines the infrastructure configuration
2. A Launch Template is created for EC2 configuration
3. An Auto Scaling Group is deployed using the launch template
4. The Auto Scaling Group launches an EC2 instance
5. Health checks continuously monitor the instance
6. If the instance fails or is terminated, Auto Scaling detects the failure
7. Auto Scaling automatically launches a new EC2 instance
8. The infrastructure maintains the desired capacity automatically

---

## Testing & Validation

- Deployed infrastructure using Terraform
- Verified Launch Template creation
- Verified Auto Scaling Group deployment
- Observed EC2 instance running under Auto Scaling
- Simulated failure by terminating the EC2 instance
- Verified Auto Scaling automatically launched a new replacement instance
- Confirmed self-healing behavior of the infrastructure

---

## Key Learnings

- Infrastructure as Code using Terraform
- Designing self-healing infrastructure
- Launch Templates for EC2 configuration
- Auto Scaling Groups for resilience
- Health checks and automatic instance recovery
- Terraform infrastructure lifecycle (init → plan → apply → destroy)

---

## Status

**Completed ✅**
