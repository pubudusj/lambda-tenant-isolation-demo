import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_tenant_isolation_demo.lambda_tenant_isolation_demo_stack import LambdaTenantIsolationDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_tenant_isolation_demo/lambda_tenant_isolation_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaTenantIsolationDemoStack(app, "lambda-tenant-isolation-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
