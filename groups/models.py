import datetime
from django.db import models
import random


class Group(models.Model):
    course = models.CharField(max_length=64, null=False)  # Course name
    users = models.IntegerField(null=False)  # Amount of students in group
    start_date = models.DateField(null=False)  # Date of first lesson

    @classmethod
    def generate_courses(cls, count=6):
        occupation = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++']

        for _ in range(count):
            g = Group()
            g.course = random.choice(occupation)
            g.users = random.randint(18, 80)
            g.start_date = datetime.datetime.today()

            g.save()

    def __str__(self):
        return f"Group({self.id}): {self.course} Amount of users: {self.users} " \
               f"Started: {self.start_date}"
