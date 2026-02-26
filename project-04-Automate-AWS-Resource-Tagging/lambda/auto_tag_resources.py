import boto3

ec2 = boto3.client('ec2')

DEFAULT_TAGS = {
    "Environment": "Dev",
    "Owner": "CloudTeam",
    "CostCenter": "CC-001"
}

def lambda_handler(event, context):
    resource_id = event['detail']['resourceId']
    resource_type = event['detail']['resourceType']

    if resource_type != "AWS::EC2::Instance":
        return {"message": "Resource type not supported"}

    tags = [{"Key": k, "Value": v} for k, v in DEFAULT_TAGS.items()]

    ec2.create_tags(
        Resources=[resource_id],
        Tags=tags
    )

    return {
        "message": f"Tags applied successfully to {resource_id}"
    }
