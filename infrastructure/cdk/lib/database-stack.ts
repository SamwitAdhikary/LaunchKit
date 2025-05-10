import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as rds from "aws-cdk-lib/aws-rds";

export class DatabaseStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // VPC for database
    const vpc = new ec2.Vpc(this, "LaunchKitVPC", {
      maxAzs: 2
    });

    // RDS Postgres
    new rds.DatabaseInstance(this, "PostgresInstance", {
      engine: rds.DatabaseInstanceEngine.postgres({
        version: rds.PostgresEngineVersion.VER_15
      }),
      vpc,
      credentials: rds.Credentials.fromGeneratedSecret("admin"),
      multiAz: false,
      allocatedStorage: 20,
      maxAllocatedStorage: 100,
      publiclyAccessible: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // for dev
      deletionProtection: false
    });
  }
}
