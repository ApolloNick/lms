import django_filters
from teachers.models import Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'age': ['gte', 'lte', 'exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'occupation': ['icontains']
        }
