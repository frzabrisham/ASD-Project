# Generated by Django 4.1.7 on 2023-03-07 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0009_board_favorite_board_is_closed_list_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 8, 18, 49, 22, 9206)),
        ),
    ]
