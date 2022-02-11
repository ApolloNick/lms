import datetime
import random
from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=False)
    start_date = models.DateField(default=datetime.datetime.today)

    @classmethod
    def generate_groups(cls, count):
        names = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++', 'Goland', 'NodeJS', 'C#']
        courses = ['Basic', 'Advanced']

        for _ in range(count):
            g = Group()
            g.name = random.choice(names)
            g.course = random.choice(courses)
            g.start_date = (
                datetime.datetime.today() - datetime.timedelta(days=random.randint(30, 365))
            )
            g.save()

    def get_absolute_url(self):
        return reverse('groups:group', kwargs={'id': self.id})

    def __str__(self):
        return f"Group({self.id}): NAME {self.name} COURSE: {self.course} " \
               f"Started: {self.start_date}"
