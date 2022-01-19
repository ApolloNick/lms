from django.core.management.base import BaseCommand
from faker import Faker
from teachers.models import Teacher
import random


class Command(BaseCommand):
    help = "Function for generate teachers for project LMS "

    def add_arguments(self, parser):
        parser.add_argument("number_of_teachers", type=int, help="The amount of teachers to create")

    def handle(self, *args, **kwargs):
        number_of_teachers = kwargs['number_of_teachers']
        faker = Faker()
        occupation = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++']

        for _ in range(number_of_teachers):
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.age = random.randint(25, 50)
            t.occupation = random.choice(occupation)

            t.save()
