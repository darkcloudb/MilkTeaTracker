from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating MyUser model


class MyUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    prof_pic = models.ImageField(
        default='default.jpg',
        upload_to='pics/'
    )

    def __str__(self):
        return self.username
