import random
from django.db import models
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(null=False, default=18)

    @classmethod
    def generate_students(cls, count):
        faker = Faker()

        for _ in range(count):
            s = Student()
            s.first_name = faker.first_name()
            s.last_name = faker.last_name()
            s.age = random.randint(18, 80)

            s.save()

    def __str__(self):
        return f"Student {self.first_name} {self.last_name} " \
               f"{self.age} years, id: {self.id}"
