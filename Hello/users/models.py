from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=256)
    employee_id = models.IntegerField()
    deparment = models.CharField(max_length=256)
    laptop_id = models.CharField(max_length=256, null=True)
