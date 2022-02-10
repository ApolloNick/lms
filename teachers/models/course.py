from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=32, null=False)
    teachers = models.ManyToManyField(
        to='teachers.Teacher',
        related_name='courses'
    )

    def __str__(self):
        return f"Course {self.id}  {self.name}"
