from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Student_profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_pic = CloudinaryField('image')
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name


class student_question(models.Model):
    permission = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    Program = RichTextField(blank=True, null=True)
    upload_by = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.question


class Comment(models.Model):
    question = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    comment = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.question