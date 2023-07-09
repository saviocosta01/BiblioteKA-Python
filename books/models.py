from django.db import models


class Book(models.Model):
    class Meta:
        ordering = ["id"]

    book_name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    publication = models.DateField()
    description = models.TextField()
    publishing_company = models.CharField(max_length=60)
    number_of_followers = models.IntegerField(default=0)
    follow = models.BooleanField(default=False)
    users = models.ManyToManyField("users.UserModel", related_name="books")


