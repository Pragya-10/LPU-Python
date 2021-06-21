from django.db import models
from django.db.models.base import Model

# Create your models here.

# ORM -> Object Relational Mapping
# It is the implementation which helps us
# map the operations in a database
# with the constructs in python



# HW: Create a student table and batch table without index
# in Postgres and use EXPLAIN ANALYZE to check how your
# query is running then add index and check again.


class Batch(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    roll_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()

    batch = models.ForeignKey("Batch", null=True, blank=False, on_delete=models.CASCADE, related_name="student_batch")

    def __str__(self):
        return self.name

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

