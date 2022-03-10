import datetime
import random
from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker
from core_lms.models import Person


class Teacher(Person):
    group = models.ForeignKey(
        to='groups.Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='teachers',
    )

    class PositionLevel(models.IntegerChoices):
        TEACHER = 1, 'Teacher'
        MENTOR = 2, 'Mentor'

    position = models.PositiveIntegerField(default=PositionLevel.TEACHER,
                                           choices=PositionLevel.choices)

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()
        occupation = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++']
        mobile_operators_ukr = ['050', '096', '097', '073', '048', '067', '099', '093']

        for _ in range(count):
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.age = random.randint(25, 50)
            t.occupation = random.choice(occupation)
            t.email = faker.email()
            t.birth_date = datetime.datetime.now() - relativedelta(years=t.age,
                                                                   months=random.randint(1, 12),
                                                                   days=random.randint(1, 30))
            core_number = ''
            for x in range(7):
                core_number += str(random.randint(0, 9))
            t.phone_number = f'+38({random.choice(mobile_operators_ukr)}){core_number}'

            t.save()

    def __str__(self):
        return f"Teacher {self.id}  {self.first_name} {self.last_name} " \
               f"{self.age} years, {self.birth_date}  {self.occupation} specialist, " \
               f"Phone: {self.phone_number} Email: {self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
