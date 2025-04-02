from django.db import models
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    poster_image = models.ImageField(upload_to='movie_posters/', null=True, blank=True) #outsorced code

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})
