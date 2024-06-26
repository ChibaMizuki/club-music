from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField()
    url2 = models.URLField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    number = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.number}: {self.title} by {self.artist} (Added on {self.created_at})"
