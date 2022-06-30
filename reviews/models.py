from tkinter import CASCADE

from django.db import models


class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(False)
    recomendation = models.CharField(max_length=50)
    
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name='movies'
    )
    
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='users'
    )
    
    
