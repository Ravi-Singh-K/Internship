import datetime
from django.db import models
from django.utils import timezone

from mysite.polls import admin

# Create your models here.
class Question(models.Model):

    question_text = models.CharField(max_length = 200)
    pub_date = models.DateField("Date Published", auto_now_add=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    @property
    def get_full_name(self):
        return self.first_name + self.last_name
    
    @admin.display(
        boolean = True,
        ordering = "pub_date",
        description = "Published recently ?",
    )

    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    def __str__(self):
        return self.question_text

class Choice(models.Model):

    question_foreign = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



# # Many to one Relationship Models

# class Manufacturer(models.Model):
#     pass
# class Car(models.Model):
#     # manufacturer = models.ForeignKey(
#     #     Manufacturer, 
#     #     on_delete=models.CASCADE
#     # )
#     company_that_makes_it = models.ForeignKey(
#         Manufacturer,
#         on_delete=models.CASCADE
#     ) # here field name can be anything but class or model name with lowercase is preferred
#     pass

# # possible values in ForeignKey arguements
# class Artist(models.Model):
#     name = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

# class Album(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

# class Song(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     album = models.ForeignKey(Album, on_delete=models.RESTRICT)

# # Artist can be deleted even if that implies deleting an Album which is referenced by a Song, because Song also references Artist itself through a cascading relationship.



# # Many to many Relationship
# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ['title']
    
#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ["headline"]

#     def __str__(self):
#         return self.headline



# F() and Q()
class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Bookdata(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=500)

    def __str__(self):
        return self.chapter_name
    

# For Conditional Expression
class Client(models.Model):
    REGULAR = "R"
    GOLD = "G"
    PLATINUM = "P"
    ACCOUNT_TYPE_CHOICES = {
        REGULAR: "Regular",
        GOLD: "Gold",
        PLATINUM: "Platinum",
    }
    name = models.CharField(max_length=50)
    registered_on = models.DateField()
    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=REGULAR,
    )

    