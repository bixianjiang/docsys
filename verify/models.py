from django.db import models

# Create your models here.
class Staff(models.Model):
    email = models.CharField(max_length = 99)
    name = models.CharField(max_length = 99)
    password = models.CharField(max_length = 99)
    status = models.IntegerField()
