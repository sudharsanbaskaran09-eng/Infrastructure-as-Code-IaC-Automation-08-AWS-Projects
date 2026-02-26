import json

def lambda_handler(event, context):
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event.get('configurationItem')

    required_tags = ["Environment", "Owner", "CostCenter"]
    resource_tags = configuration_item.get("tags", {})

    missing_tags = [tag for tag in required_tags if tag not in resource_tags]

    if missing_tags:
        compliance_type = "NON_COMPLIANT"
        annotation = f"Missing tags: {', '.join(missing_tags)}"
    else:
        compliance_type = "COMPLIANT"
        annotation = "All required tags are present"

    return {
        "complianceType": compliance_type,
        "annotation": annotation
    }
