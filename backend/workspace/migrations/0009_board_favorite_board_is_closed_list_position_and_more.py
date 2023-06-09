# Generated by Django 4.1.7 on 2023-03-07 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0008_alter_card_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='favorite',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='is_closed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 8, 18, 48, 23, 321063)),
        ),
    ]
