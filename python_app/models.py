from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Language(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Sub_topic(models.Model):
    sub_topic = models.CharField(max_length=255)

    def __str__(self):
        return self.sub_topic


class tut(models.Model):
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, default='Python')
    sub_topic = models.ForeignKey(
        Sub_topic, on_delete=models.CASCADE, default='python')
    title = models.CharField(max_length=255)
    code = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class practice_set(models.Model):
    questions = models.CharField(max_length=255)
    program = RichTextField(blank=True, null=True)
