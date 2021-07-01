import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1"]
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(',')

    MONIO_HOST = os.environ.get("MONIO_HOST")
    MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
