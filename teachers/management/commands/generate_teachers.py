from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = "Function for generate teachers for project LMS "

    def add_arguments(self, parser):
        parser.add_argument("number_of_teachers", type=int, help="The amount of teachers to create")

    def handle(self, *args, **kwargs):
        number_of_teachers = kwargs['number_of_teachers']

        for _ in range(number_of_teachers):
            Teacher.generate_teachers(number_of_teachers)
