from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50, default="Blank")
    last_name = models.CharField(max_length=50, default="Blank")
    username = models.CharField(max_length=100, unique=True)

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    @get_fullname.setter
    def set_name(self, first_name):
        self.firstname = first_name

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    language = models.CharField(max_length = 50)
    email = models.EmailField(max_length=70, blank=True, unique=True)

    def __str__(self):
        return str(self.email)