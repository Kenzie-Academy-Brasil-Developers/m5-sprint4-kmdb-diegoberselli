from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=127)
    premiere = models.DateField()
    duration = models.CharField(max_length=10)
    classification = models.IntegerField()
    synopsis = models.TextField()
    
    genre = models.ManyToManyField('genres.Genre', related_name="genres")