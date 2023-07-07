# Generated by Django 4.2.3 on 2023-07-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150, unique=True)),
                ('author', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('publication', models.DateField()),
                ('description', models.TextField()),
                ('publishing_company', models.CharField(max_length=60)),
                ('number_of_followers', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
