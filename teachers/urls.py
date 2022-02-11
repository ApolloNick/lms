from django.urls import path
from teachers.views import TeacherEditView, TeacherCreateView, TeacherDeleteView, get_teachers

app_name = 'teachers'

urlpatterns = [
    path("", get_teachers, name='list_teachers'),
    path("create/", TeacherCreateView.as_view(), name='create_teachers'),
    path("edit/<int:id>", TeacherEditView.as_view(), name='edit_teachers'),
    path("delete/<int:id>", TeacherDeleteView.as_view(), name='delete_teachers'),
]
