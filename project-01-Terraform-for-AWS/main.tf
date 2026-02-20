terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "demo_ec2" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux (us-east-1)
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform-Demo-EC2"
  }
}
