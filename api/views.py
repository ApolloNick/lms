from api.serializers import TeacherSerializer, GroupSerializer
from rest_framework import viewsets
from groups.models import Group
from teachers.models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
