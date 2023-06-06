from django.db import models


class Cookie(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='static/img/', blank=True)

    def __str__(self):
        return self.name
