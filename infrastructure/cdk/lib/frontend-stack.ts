import * as cdk from "aws-cdk-lib";
import { Construct } from "constructs";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as cloudfront from "aws-cdk-lib/aws-cloudfront";
import * as origins from "aws-cdk-lib/aws-cloudfront-origins";

export class FrontendStack extends cdk.Stack {
    constructor(scope: Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        // S3 bucket for hosting
        const bucket = new s3.Bucket(this, "FrontendBucket", {
            websiteIndexDocument: "index.html",
            publicReadAccess: true,
            removalPolicy: cdk.RemovalPolicy.DESTROY,
            blockPublicAccess: new s3.BlockPublicAccess({
                blockPublicAcls: false,
                ignorePublicAcls: false,
                blockPublicPolicy: false,
                restrictPublicBuckets: false,
            })
        });

        // CloudFront distribution
        new cloudfront.Distribution(this, "AppDistribution", {
            defaultRootObject: "index.html",
            defaultBehavior: {
                origin: new origins.S3Origin(bucket),
                // you can further customize caching, viewerProtocolPolicy, etc. here
            }
        });
    }
}
