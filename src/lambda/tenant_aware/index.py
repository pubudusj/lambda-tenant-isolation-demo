import json
import os
import time

import boto3

counter = 0
cloudwatch = boto3.client("cloudwatch")


def handler(event, context):
    """Tenant-aware Lambda handler with per-tenant isolation."""

    global counter
    counter += 1
    tenant_id = context.tenant_id

    metric_namespace = "TenantIsolation"
    metric_name = "TenantInvocation"
    cloudwatch.put_metric_data(
        Namespace=metric_namespace,
        MetricData=[
            {
                "MetricName": metric_name,
                "Dimensions": [
                    {"Name": "TenantId", "Value": tenant_id},
                ],
                "Unit": "Count",
                "Value": 1,
            }
        ],
    )

    output = {
        "tenant": tenant_id,
        "invocation_count": counter,
    }

    # sleep 2 seconds to simulate long processing time
    # time.sleep(2)

    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }
