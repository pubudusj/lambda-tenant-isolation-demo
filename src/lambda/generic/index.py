import json
import time

counter = 0


def handler(event, context):
    """Tenant-aware Lambda handler with per-tenant isolation."""

    global counter
    counter += 1
    output = {
        "tenant": context.tenant_id,
        "invocation_count": counter,
    }
    # sleep 2 seconds to simulate long processing time
    time.sleep(2)

    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }
