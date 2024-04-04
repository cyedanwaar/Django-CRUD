from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20)
    dept = models.CharField(max_length=30)
    sem = models.IntegerField()
    ad = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.name