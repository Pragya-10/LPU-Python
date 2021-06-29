from django.db import models
from django_minio_backend import MinioBackend, iso_date_prefix

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    video_file = models.FileField(
        storage=MinioBackend(bucket_name='django-backend-dev-private'),
        upload_to=iso_date_prefix
    )

    tags = models.ManyToManyField("main.Tag")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
