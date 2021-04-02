from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    age = models.IntegerField()
    totalmarks = models.IntegerField()

