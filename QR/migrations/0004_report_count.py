# Generated by Django 3.2.7 on 2021-09-16 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QR', '0003_auto_20210916_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]