# Project: Automated EC2 Scaling Based on Load using CloudWatch & Auto Scaling

This project demonstrates how to build an **automated scaling infrastructure** using **AWS Auto Scaling and CloudWatch monitoring**.

The infrastructure automatically adjusts the number of EC2 instances based on **CPU utilization**, ensuring optimal performance during high traffic and cost efficiency during low demand.

By integrating **CloudWatch alarms with Auto Scaling policies**, the system can automatically launch new EC2 instances when load increases and terminate instances when demand drops.

---

## Architecture Overview

The solution provisions and integrates the following components:

- **Amazon EC2** to host application instances
- **EC2 Launch Template** to define instance configuration
- **Auto Scaling Group (ASG)** to dynamically manage instances
- **Amazon CloudWatch** to monitor CPU utilization
- **CloudWatch Alarms** to trigger scaling actions
- **AWS VPC default subnet** for network placement

The Auto Scaling Group continuously monitors instance performance using CloudWatch metrics.

When CPU usage exceeds the defined threshold, Auto Scaling **launches new instances**.  
When CPU usage decreases, Auto Scaling **terminates unnecessary instances**, optimizing resource usage and cost.

This architecture follows AWS best practices for **elastic scalability, high availability, and cost optimization**.

---

## Features

- Automatic infrastructure scaling based on CPU load
- Real-time monitoring using CloudWatch
- Dynamic instance scaling with Auto Scaling Groups
- Launch Templates for consistent instance configuration
- Cost optimization through scale-in and scale-out policies
- Production-style cloud infrastructure design

---

## AWS Services Used

- AWS EC2  
- AWS EC2 Launch Templates  
- AWS Auto Scaling  
- AWS CloudWatch  
- AWS VPC  

---

## Workflow

1. An EC2 instance is launched with a web server configuration
2. A Launch Template is created for consistent instance setup
3. An Auto Scaling Group is configured using the launch template
4. CloudWatch monitors CPU utilization metrics
5. CloudWatch alarms detect high or low CPU usage
6. When CPU utilization exceeds the threshold, a **scale-out policy launches a new EC2 instance**
7. When CPU utilization drops below the threshold, a **scale-in policy terminates extra instances**
8. The infrastructure automatically maintains optimal capacity

---

## Testing & Validation

- Launched EC2 instance with web server configuration
- Created Launch Template for Auto Scaling
- Configured Auto Scaling Group with scaling policies
- Created CloudWatch alarms for CPU utilization thresholds
- Installed stress tool to simulate CPU load
- Generated CPU load using the stress command
- Observed Auto Scaling automatically launching a new EC2 instance
- Verified scaling activity in Auto Scaling Group logs
- Confirmed dynamic scaling behavior of the infrastructure

---

## Key Learnings

- Implementing automated scaling using AWS Auto Scaling
- Monitoring infrastructure with CloudWatch metrics
- Designing scalable cloud infrastructure
- Using CloudWatch alarms to trigger scaling policies
- Load testing infrastructure using Linux stress tools
- Understanding dynamic scaling and cost optimization in AWS

---

## Status

**Completed ✅**
