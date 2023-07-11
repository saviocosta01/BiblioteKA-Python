# Generated by Django 4.2.3 on 2023-07-11 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0004_remove_book_users_book_user_remove_book_follow_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='follow',
        ),
        migrations.CreateModel(
            name='BookFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='follows',
            field=models.ManyToManyField(related_name='follows', through='books.BookFollow', to=settings.AUTH_USER_MODEL),
        ),
    ]
