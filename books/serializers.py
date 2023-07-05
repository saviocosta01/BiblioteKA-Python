from rest_framework import serializers
from .models import Book
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ["id",
         "book_name", 
         "author", 
         "category", 
         "publication", 
         "description", 
         "publishing_company", 
         "number_of_followers",
         "user"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "book_name": {"required": True},
            "autho": {"required": True},
            "category": {"required": True},
            "publication": {"required": True},
            "description": {"required": True},
            "publishing_company": {"required": True},
            "number_of_followers": {"required": True},
        }
