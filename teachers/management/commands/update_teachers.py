import datetime
import random
from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher


class Command(BaseCommand):
    help = "Command for update values in app teachers for project LMS "

    def handle(self, *args, **kwargs):
        qs = Teacher.objects.all()
        max_id = len(qs)
        faker = Faker()
        occupation = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++']
        mobile_operators_ukr = ['050', '096', '097', '073', '048', '067', '099', '093']
        for item in range(max_id):
            obj = Teacher.objects.filter(id=item)
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.age = random.randint(25, 50)
            t.occupation = random.choice(occupation)
            t.email = faker.email()
            t.birth_date = datetime.datetime.now() - relativedelta(years=t.age)
            core_number = ''
            for x in range(7):
                core_number += str(random.randint(0, 9))
            t.phone_number = f'+38({random.choice(mobile_operators_ukr)}){core_number}'
            obj.update(first_name=t.first_name, last_name=t.last_name, age=t.age, occupation=t.occupation,
                       email=t.email, birth_date=t.birth_date, phone_number=t.phone_number)
