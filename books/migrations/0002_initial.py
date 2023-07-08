# Generated by Django 4.2.3 on 2023-07-08 19:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
