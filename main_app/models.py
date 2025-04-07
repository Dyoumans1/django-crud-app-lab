from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

RATINGS = (
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars')
)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=500)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='actor_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('actor-detail', kwargs={'pk': self.id})

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    poster_image = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'movie_id': self.id})
    
class Review(models.Model):
    date = models.DateField('Review date')
    rating = models.IntegerField(
        choices=RATINGS,
        default=3  
    )
    comment = models.TextField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_rating_display()} on {self.date} by {self.user.username}"
        
    class Meta:
        ordering = ['-date']
