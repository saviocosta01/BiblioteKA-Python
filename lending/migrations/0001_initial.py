# Generated by Django 4.2.3 on 2023-07-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lending_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('avaliable', models.BooleanField(default=True)),
            ],
        ),
    ]
