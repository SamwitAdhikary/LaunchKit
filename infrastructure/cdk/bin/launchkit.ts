#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { DatabaseStack } from "../lib/database-stack";
import { BackendStack } from "../lib/backend-stack";
import { FrontendStack } from "../lib/frontend-stack";

const app = new cdk.App();

// Database (Postgres + Redis)
new DatabaseStack(app, "LaunchKitDatabase");

// Backend service (ECS Fargate)
new BackendStack(app, "LaunchKitBackend");

// Frontend hosting (S3 + CloudFront)
new FrontendStack(app, "LaunchKitFrontend");
