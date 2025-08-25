from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from core.models import Subject, Exam

User = get_user_model()
# Create your models here.
class Student(User):
    class Meta:
        proxy = True
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return self.first_name + " " + self.last_name 
    
class Performance(models.Model):
    class Meta:
        verbose_name = "Performance"
        verbose_name_plural = "Performances"

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"groups__name": "Student","is_active":True},)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,limit_choices_to={"status": True},)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1990),
            MaxValueValidator(datetime.date.today().year)
        ])
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,limit_choices_to={"status": True},)
    marksObtained = models.IntegerField()
    totalMarks = models.IntegerField()
    finalGrade = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.year)
