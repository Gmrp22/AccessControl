# Generated by Django 3.2.7 on 2021-09-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QR', '0002_auto_20210916_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='departure_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='access',
            name='entry_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
