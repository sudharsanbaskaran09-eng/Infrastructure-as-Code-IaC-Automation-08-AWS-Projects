# Project: AWS Infrastructure Deployment using CloudFormation

This project demonstrates how to provision and manage AWS infrastructure using **AWS CloudFormation**. The entire infrastructure is defined as code using a YAML template and deployed as a reusable, version-controlled stack.

The stack creates a complete backend setup including networking, compute, and database resources in an automated and repeatable way.

---

## Architecture Overview
- A custom Virtual Private Cloud (VPC) is created
- Public subnets are provisioned inside the VPC
- Security Groups control inbound and outbound traffic
- An EC2 instance is launched inside the VPC
- An Amazon RDS MySQL database is deployed in private subnets
- All resources are managed by a single CloudFormation stack

This approach ensures consistency, scalability, and easy teardown or updates.

---

## Features
- Infrastructure as Code using YAML
- Fully automated resource provisioning
- Reproducible and version-controlled deployments
- Centralized stack management
- Easy rollback on failures
- Production-style AWS architecture

---

## AWS Services Used
- AWS CloudFormation
- Amazon EC2
- Amazon VPC
- Amazon RDS (MySQL)
- Security Groups
- Subnets
- AWS IAM

---

## Workflow
1. CloudFormation template is written in YAML
2. Stack is created using the AWS Console
3. CloudFormation provisions VPC, subnets, and security groups
4. EC2 instance is launched inside the VPC
5. RDS MySQL database is created in private subnets
6. Stack reaches CREATE_COMPLETE state

---

## Testing & Validation
- Stack creation monitored via CloudFormation Events
- Resource status verified in EC2, VPC, and RDS dashboards
- Confirmed CREATE_COMPLETE with no rollback
- Verified successful dependency handling between resources

---

## Key Learnings
- Writing Infrastructure as Code with CloudFormation
- Managing dependencies between AWS resources
- Designing secure VPC networking
- Automating EC2 and RDS provisioning
- Debugging CloudFormation stack failures
- Understanding rollback and stack lifecycle

---

## Status
Completed ✅
