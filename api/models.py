from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=20)
    #address = models.CharField(max_length=40)
    age = models.IntegerField()
    totalmarks = models.IntegerField()

class State(models.Model):
    user = models.ForeignKey(Stu,on_delete = models.CASCADE , related_name='addr_set')
    state = models.CharField(max_length=30)


