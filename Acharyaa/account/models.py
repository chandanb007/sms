from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    # Add any extra fields common to all users
    mobile = models.CharField(max_length=15, blank=True, null=True)
    ROLE_CHOICES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("staff", "Staff"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
