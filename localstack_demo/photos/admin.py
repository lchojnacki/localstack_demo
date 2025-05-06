from django.contrib import admin

from localstack_demo.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("uuid", "file")
