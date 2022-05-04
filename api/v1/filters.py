import django_filters
from groups.models import Group
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


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['icontains'],
            'course': ['icontains'],
        }
