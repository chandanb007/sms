from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

# Create your models here.
class Parent(User):
    class Meta:
        proxy = True
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return self.first_name + " " + self.last_name 