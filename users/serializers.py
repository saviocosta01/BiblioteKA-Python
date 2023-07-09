from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from lending.models import Lending
from users.models import UserModel
from django.contrib.auth.hashers import make_password


class LendingUser(ModelSerializer):
    class Meta:
        model = Lending
        fields = [
            "id",
            "lending_date",
            "expiration_date",
            "avaliable",
        ]
        read_only_fields = [
            "id",
            "lending_date",
            "expiration_date",
            "avaliable",
        ]


class UserSerializer(ModelSerializer):
    lendings = LendingUser(many=True, read_only=True)

    def create(self, validated_data: dict):
        category_selection = validated_data.get("category")
        if category_selection == "ESTUDANTE":
            return UserModel.objects.create_user(**validated_data)
        elif category_selection == "CONTRIBUIDOR DA BIBLIOTECA":
            return UserModel.objects.create_superuser(**validated_data)

    def update(self, instance, validated_data: dict):
        validated_data.pop("category", instance.category)
        for key, value in validated_data.items():
            if key == "password":
                value = make_password(validated_data[key])
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "address",
            "category",
            "password",
            "last_login",
            "is_superuser",
            "date_joined",
            "lending_acess",
            "lendings",
        ]
        depth = 2
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=UserModel.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=UserModel.objects.all(),
                        message="A user with that email already exists.",
                    )
                ]
            },
        }
        read_only_fields = [
            "id",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "lending_acess",
            "lendings",
        ]


class RetrieveLendingUser(ModelSerializer):
    lendings = LendingUser(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "email",
            "address",
            "category",
            "lending_acess",
            "lendings",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
            "address",
            "category",
            "lending_acess",
            "lendings",
        ]


class CreateLendingUser(ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "email",
            "category",
            "lending_acess",
        ]
        read_only_fields = [
            "id",
            "username",
            "email",
            "category",
            "lending_acess",
        ]


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField()