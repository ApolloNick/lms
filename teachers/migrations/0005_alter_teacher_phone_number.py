# Generated by Django 3.2.11 on 2022-02-06 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=24, validators=[django.core.validators.RegexValidator('^(\\+\\d\\d?)?\\(\\d{3}\\)(\\d-?){7}$', message='Phone number has to be like +38(050)111-11-11')]),
        ),
    ]