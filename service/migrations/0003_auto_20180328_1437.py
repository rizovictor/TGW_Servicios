# Generated by Django 2.0.3 on 2018-03-28 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20180328_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date_a',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 28, 19, 37, 5, 165837, tzinfo=utc)),
        ),
    ]
