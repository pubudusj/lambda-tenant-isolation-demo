import json

counter = 0


def handler(event, context):
    """Tenant-aware Lambda handler with per-tenant isolation."""

    global counter
    counter += 1
    output = {
        "tenant": context.tenant_id,
        "invocation_count": counter,
    }

    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }
