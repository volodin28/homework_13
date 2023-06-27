import uuid

from django.db import models


def upload_images(instance, filename):
    return f"static/img/{uuid.uuid4()}/{filename}"


class Cookie(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_images, null=True)

    def __str__(self):
        return self.name
