from rest_framework import serializers
from .models import Lending
from datetime import date, timedelta
import calendar

from rest_framework.fields import CurrentUserDefault
from users.serializers import CreateLendingUser
from copies.serializers import CopiesSerializer
from django.core.exceptions import PermissionDenied


class LendingSerializer(serializers.ModelSerializer):
    user = CreateLendingUser(read_only=True, default=CurrentUserDefault())
    copies = CopiesSerializer(read_only=True)

    class Meta:
        model = Lending
        fields = "__all__"
        read_only_fields = [
            "id",
            "lending_date",
            "expiration_date",
            "avaliable",
            "lock_time",
            "user",
            "copies",
        ]

    def create(self, validadet_data):
        user_logged = self.context["request"].user
        days_to_return = 3
        expiration_date = date.today() + timedelta(days=days_to_return)

        if expiration_date.weekday() == calendar.SATURDAY:
            days_to_return += 2

        elif expiration_date.weekday() == calendar.SUNDAY:
            days_to_return += 1

        expiration_date = date.today() + timedelta(days=days_to_return)

        lendings_data = Lending.objects.filter(user=user_logged)

        for i in lendings_data:
            if i.avaliable and date.today() > i.expiration_date:
                i.lock_time = 2
                user_logged.lending_acess = False
                user_logged.save()
                i.save()
                raise PermissionDenied()

        return Lending.objects.create(expiration_date=expiration_date, **validadet_data)


class DevolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["avaliable"]
