import json

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Tests the Lambda function in LocalStack"

    def add_arguments(self, parser):
        parser.add_argument(
            "--function-name",
            type=str,
            default="add-two-numbers-function",
            help="Name of the Lambda function to test",
        )

    def handle(self, *args, **options):
        function_name = options["function_name"]

        # Create Lambda client using boto3
        lambda_client = boto3.client(
            "lambda",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_ENDPOINT_URL,
            region_name=settings.AWS_DEFAULT_REGION,
        )
        self.stdout.write("\nTesting the Lambda function...")
        test_event = {"num1": 5, "num2": 7}

        invoke_response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
            Payload=json.dumps(test_event),
        )

        payload = invoke_response["Payload"].read().decode("utf-8")
        self.stdout.write(self.style.SUCCESS(f"Lambda function test result: {payload}"))
