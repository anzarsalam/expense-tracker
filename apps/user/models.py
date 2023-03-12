from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    email_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
