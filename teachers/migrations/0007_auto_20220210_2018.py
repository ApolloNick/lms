# Generated by Django 3.2.11 on 2022-02-10 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20220206_1619'),
        ('teachers', '0006_teacher_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='groups.group'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('teachers', models.ManyToManyField(related_name='courses', to='teachers.Teacher')),
            ],
        ),
    ]
