from rest_framework import serializers
from .models import Lending
from datetime import date, timedelta
import calendar
from users.serializers import UserSerializer, RetrieveLendingUser
from rest_framework.fields import CurrentUserDefault
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from users.models import UserModel


class LendingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Lending
        fields = "__all__"
        read_only_fields = [
            "id",
            "lending_date",
            "expiration_date",
            "avaliable",
            "user",
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

        # if date.today() > expiration_date:
        #     user_logged.lending_acess = False
        #     user_logged.save()
        #     raise PermissionDenied()

        return Lending.objects.create(expiration_date=expiration_date, **validadet_data)


class DevolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["avaliable"]

    def update(self, instance, validated_data):
        instance.avaliable = False
        instance.save()
        return instance
