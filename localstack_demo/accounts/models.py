from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from localstack_demo.accounts.managers import CustomUserManager
from localstack_demo.core.models import BaseModel


class CustomUser(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self) -> str:
        return self.email
