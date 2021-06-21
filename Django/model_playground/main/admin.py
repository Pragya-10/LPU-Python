from django.contrib import admin
from main.models import (
    Student,
    Pizza,
    Topping
)

# Register your models here.
admin.site.register([Student, Pizza, Topping])
