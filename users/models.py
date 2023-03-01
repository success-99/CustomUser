from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Vacancy

class CustomUser(AbstractUser):
    city = models.CharField(max_length=150)

    def __str__(self):
        return str(self.username)


class Saved(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    universitet = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user1
