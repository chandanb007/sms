from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
User = get_user_model()

class Media(models.Model):
    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Medias"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")  # or ImageField
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f"Media for {self.content_object} - {self.file.name}"

class Country(models.Model):
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=255)
    iso = models.CharField(max_length=2)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class DietaryNeed(models.Model):
    class Meta:
        verbose_name = "DietaryNeed"
        verbose_name_plural = "Dietary Needs"
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 


class Language(models.Model):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Religion(models.Model):
    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religions"
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Subject(models.Model):
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name 


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    title = models.CharField(max_length=255)    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.title

class Exam(models.Model):
    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Comment(models.Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"






