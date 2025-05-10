terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

# (Optional) Uncomment and configure to use a remote backend for state
# backend "s3" {
#   bucket = "my-terraform-state-bucket"
#   key    = "launchkit/dev/terraform.tfstate"
#   region = "us-east-1"
# }

provider "aws" {
  region = var.aws_region
}

module "ec2" {
  source        = "../../modules/ec2"
  instance_type = var.instance_type
  name          = "launchkit-dev-app"
}
