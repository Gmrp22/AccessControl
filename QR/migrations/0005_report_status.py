# Generated by Django 3.2.7 on 2021-09-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QR', '0004_report_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(default='Open', max_length=100),
        ),
    ]
