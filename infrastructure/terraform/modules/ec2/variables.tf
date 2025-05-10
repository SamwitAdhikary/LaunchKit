// infrastructure/terraform/modules/ec2/variables.tf
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "launchkit-app"
}
