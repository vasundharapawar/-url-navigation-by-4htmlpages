from django.db import models
from django.core import validators
from django import forms
# Create your models here.
def validator_for_(data):

    if data.lower().startswith('a'):
        raise forms.ValidationError('starts with a')


class Student(models.Model):

    Sname=models.CharField(max_length=100,primary_key=True)
    Sage=models.IntegerField()
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    

    def __str__(self):
        return self.Sname