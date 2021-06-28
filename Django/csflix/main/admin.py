from django.contrib import admin
from main.models import (
    Tag,
    UserInterests
)

# Register your models here.
admin.site.register([
    Tag,
    UserInterests
])