# Project: Self-Healing Infrastructure using Terraform & AWS Auto Scaling

This project demonstrates how to build a **self-healing cloud infrastructure** using **Terraform and AWS Auto Scaling**.  
The infrastructure automatically replaces unhealthy EC2 instances, ensuring **high availability and fault tolerance** without manual intervention.

The entire environment is provisioned using **Infrastructure as Code (IaC)**, making the deployment reproducible, scalable, and production-ready.

---

# Architecture Overview

The infrastructure consists of the following components:

- **Terraform** for Infrastructure as Code
- **AWS EC2 Launch Template** to define instance configuration
- **AWS Auto Scaling Group (ASG)** to maintain instance health
- **AWS EC2 Instances** that automatically recover when failures occur

If an EC2 instance fails a health check, the Auto Scaling Group **automatically terminates the unhealthy instance and launches a new one**, maintaining the desired capacity.

---

# Architecture Flow

Launch Template  
↓  
Auto Scaling Group  
↓  
EC2 Instance Running  
↓  
Health Check Monitoring  
↓  
Instance Failure Detected  
↓  
Auto Scaling Terminates Instance  
↓  
New EC2 Instance Automatically Created

---

# Features

- Infrastructure fully provisioned using Terraform
- Self-healing EC2 infrastructure
- Automatic instance replacement on failure
- Highly available architecture design
- Scalable cloud infrastructure
- Infrastructure lifecycle management

---

# AWS Services Used

- Amazon EC2
- Amazon EC2 Launch Templates
- Amazon EC2 Auto Scaling
- Amazon VPC (default)

---

# Project Structure

```
terraform-self-healing-asg/
│
├── provider.tf
├── main.tf
├── variables.tf
├── outputs.tf
│
├── SCREENSHOTS/
│
└── ARCHITECTURE.png
```

---

# Terraform Configuration

### Provider Configuration
Defines AWS as the cloud provider and the region where resources will be deployed.

### Launch Template
Defines the EC2 configuration including:

- AMI ID
- Instance Type
- Tags
- Instance configuration

### Auto Scaling Group
Maintains a desired number of EC2 instances and performs automatic healing.

Configuration includes:

- Minimum capacity
- Maximum capacity
- Desired capacity
- Health check type
- Launch template reference

---

# Deployment Steps

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/terraform-self-healing-asg.git
cd terraform-self-healing-asg
```

---

### 2️⃣ Initialize Terraform

```bash
terraform init
```

This downloads the required Terraform providers.

---

### 3️⃣ Preview Infrastructure

```bash
terraform plan
```

Shows what resources will be created.

---

### 4️⃣ Deploy Infrastructure

```bash
terraform apply
```

Type:

```
yes
```

Terraform will create:

- Launch Template
- Auto Scaling Group
- EC2 Instance

---

# Testing Self-Healing

To test the self-healing capability:

1. Go to AWS EC2 Console
2. Terminate the running EC2 instance
3. Navigate to Auto Scaling Group
4. Observe that a **new EC2 instance is automatically created**

This demonstrates **self-healing infrastructure behavior**.

---

# Infrastructure Cleanup

To delete all resources created by Terraform:

```bash
terraform destroy
```

Type:

```
yes
```

This prevents unnecessary AWS costs.

---

# Key Learnings

- Infrastructure as Code with Terraform
- Launch Templates for EC2 configuration
- Auto Scaling Groups for resilience
- Self-healing cloud infrastructure
- Terraform workflow (init → plan → apply → destroy)

---

# Real World Use Case

Self-healing infrastructure is widely used in production environments to:

- Maintain application availability
- Reduce downtime
- Automatically recover from failures
- Ensure scalable infrastructure

This approach is commonly used by **DevOps and SRE teams** in large-scale cloud environments.

---

# Status

Project Completed
