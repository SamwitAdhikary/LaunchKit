import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecr from "aws-cdk-lib/aws-ecr";

export class BackendStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // VPC and ECS cluster
    const vpc = new ec2.Vpc(this, "BackendVPC", { maxAzs: 2 });
    const cluster = new ecs.Cluster(this, "BackendCluster", { vpc });

    // Assume image is already in ECR named "launchkit-backend"
    const repo = ecr.Repository.fromRepositoryName(this, "BackendRepo", "launchkit-backend");

    // Fargate task definition
    const taskDef = new ecs.FargateTaskDefinition(this, "TaskDef", {
      cpu: 512,
      memoryLimitMiB: 1024
    });

    taskDef.addContainer("AppContainer", {
      image: ecs.ContainerImage.fromEcrRepository(repo),
      logging: ecs.LogDrivers.awsLogs({ streamPrefix: "launchkit-backend" }),
      portMappings: [{ containerPort: 8000 }]
    });

    // Fargate service
    new ecs.FargateService(this, "BackendService", {
      cluster,
      taskDefinition: taskDef,
      desiredCount: 1
    });
  }
}
