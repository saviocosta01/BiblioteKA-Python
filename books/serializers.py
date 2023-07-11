from rest_framework import serializers
from .models import Book, BookFollow
from users.serializers import CreateLendingUser, UserFollowSerializder


class BookFollowSerializer(serializers.ModelSerializer):
    #user= UserFollowSerializder(read_only=True)
    class Meta:
        model = BookFollow
        fields = [
            "id",
            "user_id",
            "book_id",
        ]
        read_only_fields = ["id", "user_id", "book_id"]

class BookSerializer(serializers.ModelSerializer):
    user = CreateLendingUser(read_only=True)
    follows = BookFollowSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "book_name",
            "author",
            "category",
            "publication",
            "description",
            "publishing_company",
            "follows",
            "number_of_followers",
            "user",
        ]
        read_only_fields = ["id", "number_of_followers", "publication","follows", "user"]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.number_of_followers += 1
        instance.save()

        return instance


class BookCopiesSerializer(serializers.ModelSerializer):
    users = CreateLendingUser(read_only=True, many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "book_name",
            "users",
        ]
        read_only_fields = ["id", "users"]