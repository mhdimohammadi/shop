# Generated by Django 5.0.3 on 2024-05-24 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_shopuser_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 10, 49, 23, 844975, tzinfo=datetime.timezone.utc)),
        ),
    ]
