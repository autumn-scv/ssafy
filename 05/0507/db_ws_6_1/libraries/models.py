from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    nickname = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
    subscribed_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribed_users')

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)