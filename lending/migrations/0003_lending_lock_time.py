from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lending',
            name='lock_time',
            field=models.IntegerField(default=0),
        ),
    ]