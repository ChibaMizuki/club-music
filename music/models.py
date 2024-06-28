from django.db import models
from django.contrib.auth.models import AbstractUser

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    url2 = models.URLField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    number = models.PositiveIntegerField(unique=True , null=False, default=0)
    
    def __str__(self):
        return f"{self.number}: {self.title} by {self.artist} (Added on {self.created_at})"
