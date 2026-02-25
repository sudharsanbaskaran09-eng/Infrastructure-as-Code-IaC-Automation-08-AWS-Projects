# Project: AWS Infrastructure Deployment using AWS CDK

This project demonstrates how to provision and manage AWS infrastructure using **AWS Cloud Development Kit (CDK)** with **TypeScript**.  
The entire infrastructure is defined as code and deployed as a reusable, version-controlled CDK stack.

The project provisions a complete backend setup including networking, serverless compute, API exposure, and database resources in an automated and repeatable way.

---

## Architecture Overview

The AWS CDK stack provisions the following components:

- A custom **Virtual Private Cloud (VPC)** spanning multiple Availability Zones
- An **Amazon S3 bucket** with versioning enabled
- An **AWS Lambda function** deployed inside the VPC
- **Amazon API Gateway** exposing the Lambda as a REST API
- An **Amazon RDS MySQL database** deployed in private subnets
- All resources managed and orchestrated using a single CDK stack

This architecture follows AWS best practices for security, scalability, and infrastructure automation.

---

## Features

- Infrastructure as Code (IaC) using AWS CDK
- TypeScript-based infrastructure definition
- Fully automated AWS resource provisioning
- Reproducible and version-controlled deployments
- Serverless architecture with API Gateway and Lambda
- Secure VPC-based database deployment
- Easy updates and stack teardown

---

## AWS Services Used

- AWS CDK (TypeScript)
- Amazon VPC
- Amazon S3
- AWS Lambda
- Amazon API Gateway
- Amazon RDS (MySQL)
- AWS IAM

---

## Workflow

1. AWS CDK application is written in TypeScript
2. CDK stack defines networking, compute, and database resources
3. CDK synthesizes the stack into CloudFormation templates
4. Stack is deployed using CDK deployment commands
5. AWS provisions all resources in the correct order
6. REST API endpoint is exposed via API Gateway
7. Stack reaches the **CREATE_COMPLETE** state

---

## Testing & Validation

- CDK synthesis verified using `cdk synth`
- Stack deployment monitored using CDK and CloudFormation
- Resources validated in:
  - VPC Dashboard
  - S3 Console
  - Lambda Console
  - API Gateway Console
  - RDS Dashboard
- Verified successful API response from Lambda
- Confirmed stack deployment with no rollback

---

## Key Learnings

- Writing Infrastructure as Code using AWS CDK
- Understanding CDK constructs and stacks
- Deploying serverless applications with Lambda and API Gateway
- Creating and managing VPC-based architectures
- Provisioning managed databases using CDK
- Comparing CDK with Terraform and CloudFormation
- Understanding CDK to CloudFormation workflow

---

## Status

**Completed ✅**
