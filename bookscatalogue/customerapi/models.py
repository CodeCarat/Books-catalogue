from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class CustomerProfile(AbstractUser):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # country = models.CharField(max_length=25)
    country = CountryField(blank_label='(select country)')
    
    def __str__(self):
        return self.email