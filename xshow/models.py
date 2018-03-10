from django.db import models

# Create your models here.
class User(models.Model):
	UserId=models.CharField(max_length=200)
	Password=models.CharField(max_length=200)