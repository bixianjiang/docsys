from django.db import models

# Create your models here.
class Doc(models.Model):
    origin = models.IntegerField()
    user = models.IntegerField()
    time = models.IntegerField()
