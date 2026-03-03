import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    print("Starting EC2 AutoStop evaluation...")

    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            
            instance_id = instance['InstanceId']
            state = instance['State']['Name']

            # Check instance state
            if state != 'running':
                continue

            # Extract tags
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

            # Validate AutoStop tag
            if tags.get('AutoStop') != 'true':
                continue

            print(f"Evaluating instance: {instance_id}")

            # Fetch CPU utilization metrics (last 10 minutes)
            cpu_metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.utcnow() - timedelta(minutes=10),
                EndTime=datetime.utcnow(),
                Period=300,
                Statistics=['Average']
            )

            if not cpu_metrics['Datapoints']:
                print(f"No CPU data for {instance_id}")
                continue

            avg_cpu = cpu_metrics['Datapoints'][0]['Average']
            print(f"Average CPU for {instance_id}: {avg_cpu}")

            # Stop instance if CPU < 5%
            if avg_cpu < 5:
                print(f"Stopping instance {instance_id} due to low CPU usage.")
                ec2.stop_instances(InstanceIds=[instance_id])
            else:
                print(f"Instance {instance_id} CPU above threshold. Skipping.")
