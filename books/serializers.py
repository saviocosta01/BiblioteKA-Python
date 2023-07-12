from rest_framework import serializers
from .models import Book, BookFollow
from users.serializers import CreateLendingUser, UserFollowSerializer


class BookFollowSerializer(serializers.ModelSerializer):
    user= UserFollowSerializer(read_only=True)
    
    class Meta:
        model = BookFollow
        fields = [
            "id",
            "user",
            "book_id",
        ]
        read_only_fields = ["id", "user", "book_id"]

class BookSerializer(serializers.ModelSerializer):
    user = CreateLendingUser(read_only=True)
    follows = BookFollowSerializer(read_only=True, many=True, source="bookfollow_set")

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
            "user",
        ]
        read_only_fields = ["id", "publication","follows", "user"]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
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