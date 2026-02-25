import { Stack, StackProps, RemovalPolicy } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as rds from 'aws-cdk-lib/aws-rds';

export class AwsCdkProjectStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // --------------------
    // VPC
    // --------------------
    const vpc = new ec2.Vpc(this, 'MyCdkVpc', {
      maxAzs: 2,
    });

    // --------------------
    // S3 Bucket
    // --------------------
    new s3.Bucket(this, 'MyCdkBucket', {
      versioned: true,
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // --------------------
    // Lambda Function
    // --------------------
    const myLambda = new lambda.Function(this, 'MyCdkLambda', {
      runtime: lambda.Runtime.NODEJS_18_X,
      handler: 'index.handler',
      code: lambda.Code.fromInline(`
        exports.handler = async function(event) {
          return {
            statusCode: 200,
            body: JSON.stringify({
              message: "Hello from AWS CDK Lambda with VPC & RDS"
            })
          };
        };
      `),
      vpc,
    });

    // --------------------
    // API Gateway
    // --------------------
    new apigateway.LambdaRestApi(this, 'MyCdkApi', {
      handler: myLambda,
      proxy: true,
    });

    // --------------------
    // RDS (MySQL)
    // --------------------
    new rds.DatabaseInstance(this, 'MyCdkRds', {
      engine: rds.DatabaseInstanceEngine.mysql({
        version: rds.MysqlEngineVersion.VER_8_0,
      }),
      vpc,
      instanceType: ec2.InstanceType.of(
        ec2.InstanceClass.T3,
        ec2.InstanceSize.MICRO
      ),
      credentials: rds.Credentials.fromGeneratedSecret('admin'),
      allocatedStorage: 20,
      publiclyAccessible: false,
      removalPolicy: RemovalPolicy.DESTROY,
      deletionProtection: false,
    });
  }
}
