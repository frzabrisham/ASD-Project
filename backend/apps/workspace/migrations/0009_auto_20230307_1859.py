# Generated by Django 2.2.6 on 2023-03-07 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0008_joinrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='board',
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='workspace.List'),
            preserve_default=False,
        ),
    ]
