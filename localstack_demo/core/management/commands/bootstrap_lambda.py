from pathlib import Path

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a simple Lambda function in LocalStack"

    def add_arguments(self, parser):
        parser.add_argument(
            "--function-name",
            type=str,
            default="add-two-numbers-function",
            help="Name of the Lambda function to create",
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

        self.stdout.write(f"Creating Lambda function '{function_name}'...")

        # Create a temporary directory for the Lambda function code
        import shutil
        import tempfile

        temp_dir = Path(tempfile.mkdtemp())
        try:
            # Create a Python file with the Lambda function code
            lambda_code_path = temp_dir / "lambda_function.py"
            with lambda_code_path.open("w") as f:
                f.write("""
import json
def lambda_handler(event, context):
    # Get the two numbers from the event
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)

    # Calculate the sum
    result = num1 + num2

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result,
            'message': f'The sum of {num1} and {num2} is {result}'
        })
    }
""")

            # Create a zip file containing the Lambda function code
            import zipfile

            zip_path = temp_dir / "lambda_function.zip"
            with zipfile.ZipFile(zip_path, "w") as zip_file:
                zip_file.write(lambda_code_path, "lambda_function.py")

            # Read the zip file
            with zip_path.open("rb") as zip_file:
                zip_bytes = zip_file.read()

            try:
                # Create the Lambda function
                response = lambda_client.create_function(
                    FunctionName=function_name,
                    Runtime="python3.13",
                    Role="arn:aws:iam::000000000000:role/lambda-role",  # Dummy role
                    Handler="lambda_function.lambda_handler",
                    Code={"ZipFile": zip_bytes},
                    Description=(
                        "A simple Lambda function that returns the sum of two numbers"
                    ),
                    Timeout=30,
                    MemorySize=128,
                    Publish=True,
                )

                function_arn = response["FunctionArn"]
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Lambda function '{function_name}' created successfully!"
                    )
                )
                self.stdout.write(f"Function ARN: {function_arn}")

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating Lambda function: {str(e)}")
                )

        finally:
            # Clean up the temporary directory
            shutil.rmtree(temp_dir)
