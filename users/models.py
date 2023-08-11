from django.db import models
from django.contrib.auth.models import AbstractUser


class CategorySelection(models.TextChoices):
    ESTUDANTE = "ESTUDANTE"
    CONTRIBUIDOR = "CONTRIBUIDOR DA BIBLIOTECA"


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    category = models.CharField(choices=CategorySelection.choices)
    lending_acess = models.BooleanField(default=True)
