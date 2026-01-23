#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lambda_tenant_isolation_demo.lambda_tenant_isolation_demo_stack import LambdaTenantIsolationDemoStack


app = cdk.App()
LambdaTenantIsolationDemoStack(app, "LambdaTenantIsolationDemoStack")

app.synth()
