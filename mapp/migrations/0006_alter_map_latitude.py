# Generated by Django 3.2 on 2021-07-22 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0005_map_dev_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='latitude',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(-56), django.core.validators.MaxValueValidator(60)]),
        ),
    ]
