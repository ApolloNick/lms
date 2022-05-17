from django_filters.rest_framework import DjangoFilterBackend
from api.v1.filters import TeacherFilter, GroupFilter
from api.v1.pagination import TeacherPagination, GroupPagination
from api.v1.serializers import TeacherSerializer, GroupSerializer
from rest_framework import viewsets
from api.v1.throttles import AnonTeacherThrottle
from groups.models import Group
from teachers.models import Teacher
from rest_framework import filters as rest_framework_filters


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = TeacherPagination
    filter_backends = [DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter]
    filterset_class = TeacherFilter
    ordering_fields = ['id', 'first_name', 'last_name', 'age', 'occupation']
    throttle_classes = [AnonTeacherThrottle]
    search_fields = ['=first_name', '=last_name', 'age', 'occupation']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupPagination
    filter_backends = [DjangoFilterBackend,
                       rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter]
    filterset_class = GroupFilter
    ordering_fields = ['id', 'name', 'course', 'start_date']
    throttle_classes = [AnonTeacherThrottle]
    search_fields = ['=name', 'course']
    http_method_names = ['get', 'post', 'put', 'delete', 'head']
