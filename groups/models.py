import datetime
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f"Group({self.id}): NAME {self.name} COURSE: {self.course} " \
               f"Started: {self.start_date}"
