# Generated by Django 3.2.11 on 2022-02-06 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20220206_1619'),
        ('teachers', '0005_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.group'),
        ),
    ]
