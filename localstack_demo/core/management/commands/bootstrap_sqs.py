import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates SQS queue in localstack for Celery tasks"

    def add_arguments(self, parser):
        parser.add_argument(
            "--queue-name",
            type=str,
            default=settings.AWS_SQS_QUEUE_NAME,
            help=(
                f"Name of the SQS queue to create "
                f"(default: {settings.AWS_SQS_QUEUE_NAME})"
            ),
        )

    def handle(self, *args, **options):
        queue_name = options["queue_name"]

        # Create SQS client using boto3
        sqs = boto3.client(
            "sqs",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_ENDPOINT_URL,
            region_name=settings.AWS_DEFAULT_REGION,
        )

        self.stdout.write(f"Creating SQS queue '{queue_name}'...")

        try:
            # Create the queue
            sqs.create_queue(
                QueueName=queue_name,
                Attributes={
                    "VisibilityTimeout": "360",  # 6 minutes
                    "MessageRetentionPeriod": "86400",  # 1 day
                },
            )

            self.stdout.write(
                self.style.SUCCESS(f"SQS queue '{queue_name}' created successfully!")
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating SQS queue: {str(e)}"))
