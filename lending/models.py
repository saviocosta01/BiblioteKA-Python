from django.db import models
from users.models import UserModel
from copies.models import Copies

# Create your models here.


class Lending(models.Model):
    lending_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True, blank=True)
    avaliable = models.BooleanField(default=True)
    lock_time = models.IntegerField(default=0)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="lendings"
    )
    copies = models.ForeignKey(
        Copies, on_delete=models.CASCADE, related_name="lendings"
    )


# class devolution(models.Model):
#     lending = models.OneToOneField(Lending, on_delete=models.CASCADE)
#     date_return = models.DateField(auto_now_add=True)
