# Generated by Django 3.2 on 2021-04-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('scale', models.DecimalField(decimal_places=2, max_digits=4)),
                ('high_color', models.CharField(max_length=36)),
                ('low_color', models.CharField(max_length=36)),
                ('resolution', models.IntegerField()),
            ],
        ),
    ]