# Generated by Django 2.2.6 on 2023-03-08 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0013_auto_20230308_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 2, 6, 7, 880783)),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(default=None, max_length=10000, null=True),
        ),
    ]
