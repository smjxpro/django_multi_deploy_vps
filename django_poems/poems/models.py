from django.db import models


class Poem(models.Model):
    title = models.CharField(max_length=100)
    poet = models.CharField(max_length=100)
    poem = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.poet}'
