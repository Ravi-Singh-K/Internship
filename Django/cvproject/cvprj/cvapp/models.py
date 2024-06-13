from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

# Name Base Model
class BaseModel(models.Model):
    name = models.CharField(max_length=100)

GENDER = (
    ("M", "Male"),
    ("F", "Female"),
)
TYPE = (
    ("SEE", "School"),
    ("+2", "High School"),
    ("Bachelor", "College"),
    ("Master", "University"),
)

# Skill Many To Many Field
class Skill(BaseModel):

    def __str__(self): 
        return self.name
    
# Language Many To Many Field
class Language(BaseModel):
    
    def __str__(self):
        return self.name

    

# Custom User
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to="media")
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="M")
    skill = models.ManyToManyField(Skill)
    language = models.ManyToManyField(Language)

    @property
    def get_fullname(self):
        return self.first_name, " " ,self.last_name

    def get_age(self):
        year, month, day = map(int, self.birth_date.split("-"))
        today = datetime.date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        return age


class Education(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='education')
    location = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=TYPE)
    grade = models.FloatField(blank=True)
    enroll_date = models.DateField(blank=True)
    passed_date = models.DateField(blank=True)

    def __str__(self):
        return self.name

    
class PersonalInfo(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='personalinfo')
    github = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()
    aboutme = models.TextField()

    def __str__(self):
        return self.name
    

class Company(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='company')
    location = models.CharField(max_length=100)
    joined_date = models.DateField(blank=True)
    left_date = models.DateField(blank=True)

    @property
    def get_duration(self):
        year1 = self.joined_date.year
        year2 = self.left_date.year
        duration = year2 - year1
        if duration > 365:
            return duration/365
        elif 12 < duration < 365:
            return duration/12
        else:
            return duration

    def __str__(self):
        return self.name


class Achievement(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='achievement')
    platform_name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Reference(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reference')
    reference_description = models.TextField()

    def __str__(self):
        return self.name