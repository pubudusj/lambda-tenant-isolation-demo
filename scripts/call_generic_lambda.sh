#!/bin/bash

# API endpoint
ENDPOINT="[APIGW_BaseURL]/execute_tenant_aware_lambda"

while true; do
    # Generate a random tenant_id (tenant1 to tenant10)
    TENANT_ID="tenant$((RANDOM % 10 + 1))"
    echo "Calling endpoint with tenant_id: $TENANT_ID"
    curl -s "${ENDPOINT}?tenant_id=${TENANT_ID}"
    echo -e "\n"
done
