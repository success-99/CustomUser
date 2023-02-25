from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    city = models.CharField(max_length=150)

    def __str__(self):
        return str(self.username)
