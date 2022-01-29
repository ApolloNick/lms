from django.urls import path
from teachers.views import get_teachers, create_teacher, edit_teacher

urlpatterns = [
    path("", get_teachers, name='list_teachers'),
    path("create/", create_teacher, name='create_teachers'),
    path("edit/<int:id>", edit_teacher, name='edit_teachers'),
]
