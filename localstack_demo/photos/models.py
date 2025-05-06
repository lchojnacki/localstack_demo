from django.db import models

from localstack_demo.core.models import BaseModel

upload_directory = "photos"


class Photo(BaseModel):
    file = models.ImageField(upload_to=f"{upload_directory}/")
