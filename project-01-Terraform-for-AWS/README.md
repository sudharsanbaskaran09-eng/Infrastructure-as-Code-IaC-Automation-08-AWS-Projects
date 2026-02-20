# Project: Terraform for AWS Infrastructure

This project demonstrates provisioning AWS infrastructure using Terraform by applying Infrastructure as Code (IaC) principles. The infrastructure is created, managed, and destroyed entirely through code without using the AWS Management Console.

---

## Architecture Overview
- Terraform is used as the Infrastructure as Code tool
- AWS Provider connects Terraform to the AWS account
- Terraform provisions an Amazon EC2 instance
- Infrastructure state is managed using Terraform state files
- Resources are created and destroyed in a controlled manner

This architecture enables repeatable, automated, and scalable infrastructure provisioning.

---

## Features
- Infrastructure provisioning using code
- Automated EC2 instance creation
- Declarative infrastructure management
- Repeatable and consistent deployments
- Safe resource cleanup using Terraform destroy
- No manual AWS Console operations

---

## AWS Services Used
- Amazon EC2
- AWS IAM
- AWS CLI
- Terraform (AWS Provider)

---

## Workflow
1. Configure AWS credentials using AWS CLI
2. Define infrastructure using Terraform configuration files
3. Initialize Terraform working directory
4. Validate Terraform configuration
5. Review infrastructure changes using Terraform plan
6. Provision infrastructure using Terraform apply
7. Destroy infrastructure to avoid unnecessary costs

---

## Testing
- Terraform configuration validated using `terraform validate`
- Execution plan reviewed using `terraform plan`
- EC2 instance verified in AWS Console after apply
- Resource cleanup verified after terraform destroy

---

## Status
Completed ✅
