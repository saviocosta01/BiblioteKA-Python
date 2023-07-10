from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Lending
from datetime import date, timedelta
import calendar

from rest_framework.fields import CurrentUserDefault
from users.serializers import RetrieveLendingUser, CreateLendingUser
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
        print(lendings_data)

        for i in lendings_data:
            if date.today() < i.expiration_date:
                user_logged.lending_acess = False
                user_logged.save()
                raise PermissionDenied()

        return Lending.objects.create(expiration_date=expiration_date, **validadet_data)


class DevolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["avaliable"]

    def update(self, instance, validated_data):
        instance.avaliable = False
        instance.save()
        return instance


class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = "__all__"
        read_only_fields = [
            "id",
            "lending_date",
            "expiration_date",
            "avaliable",
            "user",
            "copies",
        ]

    def get(self, validadet_data):
        user_logged = self.context["request"].user
        lendings_data = Lending.objects.filter(user=user_logged)
        print(lendings_data.expiration_date, "aquiiiiiii")
        return lendings_data
