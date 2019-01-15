from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length=20)
    upassword = models.CharField(max_length=20)
    upriority = models.IntegerField()
    unickname = models.CharField(max_length=20)

