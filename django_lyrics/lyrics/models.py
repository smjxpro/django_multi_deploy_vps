from django.db import models


class Lyric(models.Model):
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    lyric = models.TextField()

    def __str__(self):
        return f'{self.song} - {self.artist}'
