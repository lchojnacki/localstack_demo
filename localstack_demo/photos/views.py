import boto3
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from localstack_demo.photos.models import Photo, upload_directory


def get_presigned_upload_url(filename, request=None):
    # Use the hostname from the request if available
    endpoint_url = settings.AWS_ENDPOINT_URL
    if request and request.get_host():
        # Extract the hostname from the request
        host = request.get_host().split(":")[0]  # Remove port if present
        # Replace the hostname in the endpoint URL
        endpoint_url = endpoint_url.replace("127.0.0.1", host)

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        endpoint_url=endpoint_url,
    )
    return s3_client.generate_presigned_url(
        "put_object",
        Params={
            "Bucket": settings.AWS_MEDIAFILES_BUCKET_NAME,
            "Key": filename,
        },
        ExpiresIn=3600,
    )


class PhotoUploadView(TemplateView):
    template_name = "photos/photo_upload.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photo.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        # Get the filename from the request (AJAX)
        filename = request.POST.get("filename")
        if not filename:
            return JsonResponse({"error": "No filename provided."}, status=400)

        # Generate the S3 key (path in bucket)
        s3_key = f"{upload_directory}/{filename}"

        presigned_url = get_presigned_upload_url(s3_key, request=request)

        Photo.objects.create(file=s3_key)

        return JsonResponse(
            {
                "url": presigned_url,
                "key": s3_key,
            }
        )
