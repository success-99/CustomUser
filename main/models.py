from django.db import models
from django.urls import reverse


# Create your models here.
class Vacancy(models.Model):
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    rank = models.CharField(max_length=100)
    gender = models.CharField(max_length=7)
    salary = models.CharField(max_length=50)



    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return reverse('vacancydetail', args=[str(self.pk)])
