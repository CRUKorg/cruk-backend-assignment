from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as aws_lambda,
)
from constructs import Construct

class AwsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        with open('lambda/example_func.py', encoding='utf8') as fp:
            lambda_code = fp.read()

        # This is just an example - feel free to delete
        example_fn = aws_lambda.Function(self,
                    id='example_fn',
                    description='A placeholder function',
                    code=aws_lambda.InlineCode(lambda_code),
                    handler='index.lambda_handler',
                    timeout=Duration.seconds(300),
                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                    environment={})
