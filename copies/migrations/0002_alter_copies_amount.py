# Generated by Django 4.2.3 on 2023-07-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copies',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]