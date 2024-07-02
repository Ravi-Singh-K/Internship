from django.db import models
from django.contrib.auth.models import User


MOVIE_GENRE = {
    'Action' : 'Act',
    'Comedy' : 'Com',
    'Animation' : 'Ani',
    'Thriller' : 'Thr',
    'Adventure' : 'Adv',
    'War' : 'War',
    'Western' : 'West',
    'Horror' : 'Hor'
}
MOVIE_LANGUAGE = {
    'Eng' : 'English',
    'Hin' : 'Hindi',
    'Nep' : 'Nepali',
    'Ita' : 'Italian',
    'Spa' : 'Spanish',
    'Kor' : 'Korean',
    'Jap' : 'Japanese'
}

# Create your models here.
class Movie(models.Model):
    owner = models.ForeignKey(User, related_name = 'movies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(choices=MOVIE_GENRE, default='Action', max_length=50)
    language = models.CharField(choices=MOVIE_LANGUAGE, default='Eng', max_length=50)
    release_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    highlighted = models.TextField(blank=True, default="Default Highlighted Text")

    class Meta:
        ordering = ['release_date']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
