from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100,blank=False)
    last_name = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
