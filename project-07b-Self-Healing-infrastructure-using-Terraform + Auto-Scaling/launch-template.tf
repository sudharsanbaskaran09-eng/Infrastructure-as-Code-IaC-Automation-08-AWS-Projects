resource "aws_launch_template" "self_healing_template" {

  name_prefix   = "self-healing-template"
  image_id      = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = "Self-Healing-ASG-Instance"
    }
  }
}
