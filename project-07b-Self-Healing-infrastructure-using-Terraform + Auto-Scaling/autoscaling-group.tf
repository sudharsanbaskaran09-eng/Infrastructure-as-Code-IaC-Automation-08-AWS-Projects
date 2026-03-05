resource "aws_autoscaling_group" "self_healing_asg" {

  name = "self-healing-asg"

  min_size         = 1
  max_size         = 2
  desired_capacity = 1

  vpc_zone_identifier = ["subnet-xxxxxxxxxxxxxxxx"]

  launch_template {
    id      = aws_launch_template.self_healing_template.id
    version = "$Latest"
  }

  health_check_type = "EC2"
}
