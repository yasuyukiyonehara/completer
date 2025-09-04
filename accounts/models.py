from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    Phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username