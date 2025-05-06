import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates S3 buckets in localstack"

    def handle(self, *args, **options):
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_ENDPOINT_URL,
        )
        self.stdout.write("Creating staticfiles bucket...")
        s3.create_bucket(Bucket=settings.AWS_STATICFILES_BUCKET_NAME)

        # Configure CORS for staticfiles bucket
        s3.put_bucket_cors(
            Bucket=settings.AWS_STATICFILES_BUCKET_NAME,
            CORSConfiguration={
                "CORSRules": [
                    {
                        "AllowedHeaders": ["*"],
                        "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
                        "AllowedOrigins": ["*"],
                        "ExposeHeaders": ["ETag"],
                        "MaxAgeSeconds": 3000,
                    }
                ]
            },
        )

        self.stdout.write("Creating mediafiles bucket...")
        s3.create_bucket(Bucket=settings.AWS_MEDIAFILES_BUCKET_NAME)

        # Configure CORS for mediafiles bucket
        s3.put_bucket_cors(
            Bucket=settings.AWS_MEDIAFILES_BUCKET_NAME,
            CORSConfiguration={
                "CORSRules": [
                    {
                        "AllowedHeaders": ["*"],
                        "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
                        "AllowedOrigins": ["*"],
                        "ExposeHeaders": ["ETag"],
                        "MaxAgeSeconds": 3000,
                    }
                ]
            },
        )
