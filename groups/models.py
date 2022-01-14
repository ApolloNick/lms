from django.db import models


class Group(models.Model):
    course = models.CharField(max_length=64, null=False)  # Course name
    users = models.IntegerField(null=False)  # Amount of students in group
    start_date = models.DateField(null=False)  # Date of first lesson
    end_date = models.DateField()  # Date of last lesson
