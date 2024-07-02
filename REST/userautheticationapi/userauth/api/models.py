from django.db import models
from django.contrib.auth.models import User


GENRE_CHOICE = [
    ('Fantasy', 'Fantasy'),
    ('Thriller', 'Thriller'),
    ('Romantic', 'Romantic'),
    ('Mystery', 'Mystery'),
    ('Biography', 'Biography')
]

# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    genre = models.CharField(choices=GENRE_CHOICE, max_length=10, default='Fantasy')
    published_date = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title