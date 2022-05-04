from rest_framework import serializers
from teachers.models import Teacher
from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'course', 'start_date')


class TeacherSerializer(serializers.ModelSerializer):
    group_obj = GroupSerializer(read_only=True, source='group')

    class Meta:
        model = Teacher
        fields = ('id', 'first_name', 'last_name', 'age', 'occupation', 'group_obj')
