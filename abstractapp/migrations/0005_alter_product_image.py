# Generated by Django 3.2.8 on 2021-10-17 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstractapp', '0004_auto_20211016_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=500, upload_to='images'),
        ),
    ]
