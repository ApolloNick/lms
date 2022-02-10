# Generated by Django 3.2.11 on 2022-02-06 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='NULL', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='start_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]