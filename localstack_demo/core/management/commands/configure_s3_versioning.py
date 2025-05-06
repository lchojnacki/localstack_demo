import boto3
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        f"Enables versioning on {settings.AWS_MEDIAFILES_BUCKET_NAME} "
        f"bucket and removes a specified file"
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "filename", type=str, help="Path to the file to delete from the S3 bucket"
        )

    def handle(self, *args, **options):
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_ENDPOINT_URL,
        )

        # Step 1: Enable versioning on the bucket
        self.stdout.write(
            f"Enabling versioning on {settings.AWS_MEDIAFILES_BUCKET_NAME} bucket..."
        )
        s3.put_bucket_versioning(
            Bucket=settings.AWS_MEDIAFILES_BUCKET_NAME,
            VersioningConfiguration={"Status": "Enabled"},
        )
        self.stdout.write(self.style.SUCCESS("Versioning enabled successfully!"))

        # Step 2: List files in the bucket before deletion
        self.stdout.write(
            self.style.SUCCESS(
                f"\nListing files in {settings.AWS_MEDIAFILES_BUCKET_NAME} bucket "
                f"BEFORE deletion:"
            )
        )
        self._list_bucket_files(s3, settings.AWS_MEDIAFILES_BUCKET_NAME)

        # Step 3: List files marked as deleted before deletion
        self.stdout.write(
            self.style.SUCCESS("\nListing files marked as deleted BEFORE deletion:")
        )
        self._list_deleted_files(s3, settings.AWS_MEDIAFILES_BUCKET_NAME)

        # Step 4: Delete the specified file
        file_to_delete = options["filename"]
        self.stdout.write(
            f"\nRemoving file {file_to_delete} "
            f"from {settings.AWS_MEDIAFILES_BUCKET_NAME} bucket..."
        )
        try:
            s3.delete_object(
                Bucket=settings.AWS_MEDIAFILES_BUCKET_NAME, Key=file_to_delete
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"File {file_to_delete} marked as deleted successfully! "
                    f"(With versioning enabled, the file is not actually "
                    f"deleted but marked as deleted)"
                )
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error deleting file: {str(e)}"))

        # Step 5: List files in the bucket after deletion
        self.stdout.write(
            self.style.SUCCESS(
                f"\nListing files in {settings.AWS_MEDIAFILES_BUCKET_NAME} bucket "
                f"AFTER deletion:"
            )
        )
        self._list_bucket_files(s3, settings.AWS_MEDIAFILES_BUCKET_NAME)

        # Step 6: List files marked as deleted after deletion
        self.stdout.write(
            self.style.SUCCESS("\nListing files marked as deleted AFTER deletion:")
        )
        self._list_deleted_files(s3, settings.AWS_MEDIAFILES_BUCKET_NAME)

    def _list_bucket_files(self, s3_client, bucket_name):
        """Helper method to list all files in a bucket"""
        try:
            response = s3_client.list_objects_v2(Bucket=bucket_name)

            if "Contents" in response:
                for obj in response["Contents"]:
                    self.stdout.write(
                        f"  - {obj['Key']} (Size: {obj['Size']} bytes, "
                        f"Last Modified: {obj['LastModified']})"
                    )
            else:
                self.stdout.write("  No files found in the bucket.")

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error listing bucket contents: {str(e)}")
            )

    def _list_deleted_files(self, s3_client, bucket_name):
        """Helper method to list all files marked as deleted in a bucket"""
        try:
            response = s3_client.list_object_versions(Bucket=bucket_name)

            delete_markers_found = False
            if "DeleteMarkers" in response:
                delete_markers_found = True
                for marker in response["DeleteMarkers"]:
                    if marker[
                        "IsLatest"
                    ]:  # Only show delete markers that are the latest version
                        self.stdout.write(
                            f"  - {marker['Key']} "
                            f"(Deleted on: {marker['LastModified']}, "
                            f"Version ID: {marker['VersionId']})"
                        )

            if not delete_markers_found:
                self.stdout.write("  No deleted files found in the bucket.")

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error listing deleted files: {str(e)}")
            )
