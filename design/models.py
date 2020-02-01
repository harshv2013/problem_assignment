from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=200)
    pan_number = models.CharField(max_length=200, unique=True, help_text='Unique Pan Number ')
    age = models.PositiveSmallIntegerField(validators= [MaxValueValidator(100)])
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    email = models.EmailField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

