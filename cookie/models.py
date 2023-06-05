from django.db import models


class Cookie(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
