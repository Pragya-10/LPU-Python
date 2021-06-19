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



# DDL vs DML
# SQL

# Remove roll number and add admission number
# name dob admission_number(not null)(primary key)

# Migrations

# -> Create Student Table

# -> Adding class column

# -> Add admission number

# -> Remove roll number and make admission number primary

# DjangoMigrationStatus
# - Create Student Table
# - Adding class column

