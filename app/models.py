from django.db import models
from django.core import validators

from django import forms


def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('first letter not should be a')

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True ,validators=[check_for_a])

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name

