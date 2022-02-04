import datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import RegexValidator
from faker import Faker
import random
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False, default="test_django@gmail.com")
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=24,
                                    validators=[RegexValidator(
                                        r'^(\+\d\d?)?\(\d{3}\)(\d-?){7}$',
                                        message='Phone number has to be like +38(050)111-11-11')])

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
