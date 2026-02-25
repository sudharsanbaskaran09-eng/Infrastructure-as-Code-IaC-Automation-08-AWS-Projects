#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { AwsCdkProjectStack } from '../lib/aws-cdk-project-stack';

const app = new cdk.App();
new AwsCdkProjectStack(app, 'AwsCdkProjectStack');
