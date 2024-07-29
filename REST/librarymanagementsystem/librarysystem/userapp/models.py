from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from .validators import passwordvalidator, contactvalidator
from .choices import BOOK_CHOICES, RETURNED_STATUS_CHOICES
from django.core.validators import RegexValidator


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    faculty = models.ManyToManyField(Faculty, related_name="books")
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=BOOK_CHOICES, default="Available")
    book_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, validators=[RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message="First name must contain only alphabets.",
        code="invalid_first_name",
    )])
    last_name = models.CharField(max_length=100, validators=[RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message="Last name must contain only alphabets.",
        code="invalid_last_name",
    )])
    profile_picture = models.ImageField(upload_to="media/profile/student/", blank=True, null=True)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=15, validators=[contactvalidator])
    primary_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups', null=True, blank=True) 
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    password = models.CharField(max_length=100, validators=[passwordvalidator, contactvalidator])

    def __str__(self):
        return self.username


class BookAssignment(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="assigns")
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="assigns")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="assigns")
    assigned_at = models.DateField(auto_now_add=True)
    status = models.CharField(choices=RETURNED_STATUS_CHOICES, max_length=8, default='Pending')
    returned_at = models.DateField(null=True, blank=True)
    overdue_charge = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.users} --> {self.book} --> {self.assigned_at}"


class RequestBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="requestbooks")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="requestbooks")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="requestbooks")
    requested_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} --> {self.book} --> {self.requested_at}"