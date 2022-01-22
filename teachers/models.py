from django.db import models
from faker import Faker
import random
from django.db import models
from phone_field import PhoneField


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False, default="test_django@gmail.com")
    birth_date = models.DateField(null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    @classmethod
    def generate_teachers(cls, count):
        faker = Faker()
        occupation = ['Python', 'Java', 'JavaScript', 'PHP', 'C', 'C++']

        for _ in range(count):
            t = Teacher()
            t.first_name = faker.first_name()
            t.last_name = faker.last_name()
            t.age = random.randint(25, 50)
            t.occupation = random.choice(occupation)

            t.save()

    def __str__(self):
        return f"Teacher {self.id}  {self.first_name} {self.last_name} " \
               f"{self.age} years, {self.occupation} specialist"