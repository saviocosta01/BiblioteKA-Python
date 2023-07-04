from django.db import models
from users.models import UserModel

# Create your models here.


class Lending(models.Model):
    lending_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="lendings",
    )


# class devolution(models.Model):
#     lending = models.OneToOneField(Lending, on_delete=models.CASCADE)
#     date_return = models.DateField(auto_now_add=True)
