from django.db import models


class Office(models.Model):
    location=models.CharField(max_length=200)
    building=models.CharField(max_length=200)
