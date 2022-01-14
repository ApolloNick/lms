from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=64, null=False)
    related_groups = models.CharField(max_length=64)

