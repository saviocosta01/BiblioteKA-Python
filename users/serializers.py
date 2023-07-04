from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from users.models import UserModel
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    def create(self, validated_data: dict):
        category_selection = validated_data.get('category')
        if category_selection == "ESTUDANTE":
            return UserModel.objects.create_user(**validated_data)
        elif category_selection == "CONTRIBUIDOR DA BIBLIOTECA":
            return UserModel.objects.create_superuser(**validated_data)
    
    def update(self, instance, validated_data:dict):
        for key, value in validated_data.items():
            if key == "password":
                value = make_password(validated_data[key])
            setattr(instance,key, value)

        instance.save()
        return instance

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address', 'category','password','last_login',"is_superuser","date_joined",'lending_acess']
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
            "is_active":{'read_only':True},
            "username": {"validators": [UniqueValidator(queryset=UserModel.objects.all(), message="A user with that username already exists.")]},
            "email": {"validators": [UniqueValidator(queryset=UserModel.objects.all(), message="A user with that email already exists.")]},
            "date_joined":{"read_only":True},
            "last_login":{"read_only":True},
            "lending_acess":{"read_only":True},
        }