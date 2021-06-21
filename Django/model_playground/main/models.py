from django.db import models
from django.db.models.base import Model

# Create your models here.

# ORM -> Object Relational Mapping
# It is the implementation which helps us
# map the operations in a database
# with the constructs in python

class Student(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()

class Pizza(models.Model):
    name = models.CharField(max_length=256)
    mrp = models.FloatField()

    toppings = models.ManyToManyField("Topping")

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

