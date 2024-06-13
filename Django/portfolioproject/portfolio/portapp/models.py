from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField(upload_to='media/', blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username

class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="education")
    school_name = models.CharField(max_length=200, blank=True, null=True)
    school_grade = models.FloatField(blank=True, null=True)
    school_passed_year = models.DateField(default=timezone.now)
    collage_name = models.CharField(max_length=200, blank=True, null=True)
    collage_grade = models.FloatField(blank=True, null=True)
    collage_passed_year = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.school_name

class Skill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.skill_name)
    
class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="experience")
    company_name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.company_name
    