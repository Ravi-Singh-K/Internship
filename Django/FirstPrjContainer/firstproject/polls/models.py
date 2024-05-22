from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
# class Author(models.Model):
#     auth_name = models.CharField(max_length = 100)
#     auth_address = models.CharField(max_length=100)
#     auth_contact = models.IntegerField(default=None)

#     def __str__(self):
#         return self.auth_name

# class Book(models.Model):
#     author = models.ManyToManyField(Author, on_update = models.CASCADE)
#     book_name = models.CharField(max_length=100)
#     published_date = models.DateField()

#     def __str__(self):
#         return self.book_name
