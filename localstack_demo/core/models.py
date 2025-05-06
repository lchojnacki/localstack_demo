import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    uuid = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, verbose_name=_("UUID")
    )

    class Meta:
        abstract = True
