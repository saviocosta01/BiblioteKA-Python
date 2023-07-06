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
        
        validated_data.pop('category', instance.category)
        for key, value in validated_data.items():
            if key == "password":
                value = make_password(validated_data[key])
            setattr(instance,key, value)
        instance.save()
        return instance
    
    class Meta:
        model = UserModel
        fields = ['id',
                   'username', 
                   'first_name', 
                   'last_name', 
                   'email', 
                   'address', 
                   'category',
                   'password',
                   'last_login',
                   "is_superuser",
                   "date_joined",
                   'lending_acess',
                   'books'
                   ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"validators": [UniqueValidator(queryset=UserModel.objects.all(), message="A user with that username already exists.")]},
            "email": {"validators": [UniqueValidator(queryset=UserModel.objects.all(), message="A user with that email already exists.")]},
        }
        read_only_fields = ["id", "is_superuser","is_active", "date_joined","last_login","lending_acess", 'books']
        
       
          
           
        
          
                

