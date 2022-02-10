from django.core.validators import RegexValidator
from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

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
