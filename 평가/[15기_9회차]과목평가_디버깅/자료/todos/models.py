from django.db import models
from django.conf import settings

# Create your models here.

class Todo(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
  title = models.CharField(max_length=100)
  content = models.TextField()
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to='todos/', blank=True)

class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
  todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)