from django.db import models

# Create your models here.
class Acc(models.Model):
    num=models.IntegerField()
    sc=models.CharField(max_length=1000)
