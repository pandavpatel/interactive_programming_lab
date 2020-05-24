from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    year_of_intake = models.PositiveIntegerField(default=0)
    password_change_required = models.BooleanField(default=True)
