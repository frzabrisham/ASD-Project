# Generated by Django 4.1.7 on 2023-02-26 14:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
