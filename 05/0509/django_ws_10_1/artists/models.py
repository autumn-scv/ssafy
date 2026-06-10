from django.db import models

# Create your models here.
class Artists(models.Model):
    name = models.CharField(max_length=20)
    agency = models.CharField(max_length=50)
    debut_date = models.DateField()
    is_group = models.BooleanField()