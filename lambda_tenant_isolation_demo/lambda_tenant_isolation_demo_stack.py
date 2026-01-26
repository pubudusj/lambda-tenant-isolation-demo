from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct


class LambdaTenantIsolationDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tenant_aware_lambda = _lambda.Function(
            self,
            "TenantAwareFunction",
            function_name="tenant-aware-lambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=_lambda.Code.from_asset("src/lambda/tenant_aware"),
            logging_format=_lambda.LoggingFormat.JSON,
            timeout=Duration.seconds(20),
            tenancy_config=_lambda.TenancyConfig.PER_TENANT,
        )

        generic_lambda = _lambda.Function(
            self,
            "GenericFunction",
            function_name="generic-lambda",
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler="index.handler",
            code=_lambda.Code.from_asset("src/lambda/generic"),
            logging_format=_lambda.LoggingFormat.JSON,
            timeout=Duration.seconds(20),
        )

        # Create API Gateway
        api = apigw.RestApi(
            self,
            "TenantIsolationApi",
            rest_api_name="Tenant Isolation Demo API",
        )

        # Lambda integration with tenant_id query param mapped to X-Amz-Tenant-Id header
        tenant_aware_integration = apigw.LambdaIntegration(
            tenant_aware_lambda,
            request_parameters={
                "integration.request.header.X-Amz-Tenant-Id": "method.request.querystring.tenant_id"
            },
        )

        # Add /execute_tenant_aware_lambda endpoint
        tenant_aware_resource = api.root.add_resource("execute_tenant_aware_lambda")
        tenant_aware_resource.add_method(
            "GET",
            tenant_aware_integration,
            request_parameters={
                "method.request.querystring.tenant_id": True,
            },
        )

        # Add /execute_generic_lambda endpoint
        generic_resource = api.root.add_resource("execute_generic_lambda")
        generic_resource.add_method(
            "GET",
            apigw.LambdaIntegration(generic_lambda),
            request_parameters={
                "method.request.querystring.tenant_id": True,
            },
        )
