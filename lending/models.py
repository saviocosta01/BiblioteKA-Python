from django.db import models

# Create your models here.


class Lending(models.Model):
    lending_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
