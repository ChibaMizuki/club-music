from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    url2 = models.URLField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    number = models.PositiveIntegerField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:  # 新規登録時のみ実行
            last_number = Song.objects.count()
            self.number = last_number + 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.number}: {self.title} by {self.artist} (Added on {self.created_at})"

# データ削除後に番号を再割り振りする
@receiver(post_delete, sender=Song)
def reorder_numbers(sender, **kwargs):
    for index, song in enumerate(Song.objects.order_by('created_at'), start=1):
        if song.number != index:
            song.number = index
            song.save()
