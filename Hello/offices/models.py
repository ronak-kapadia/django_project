from django.db import models

class Office(models.Model) :
    name=models.CharField(max_length=250)
    address= models.CharField(max_length=250)
    building=models.CharField(max_length=250)
    no_of_emp= models.IntegerField()

