from django.db import models

class Department(models.Model):
    role=models.CharField(max_length=200)
    name=models.CharField(max_length=200)


