from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Teacher(User):
    class Meta:
        proxy = True
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.first_name + " " + self.last_name 

