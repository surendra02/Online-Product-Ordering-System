# Generated by Django 3.2.8 on 2021-10-18 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0010_auto_20211018_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cuntry',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 10, 18, 15, 12, 25, 657588)),
        ),
    ]
