from django.urls import path
from students.views import get_students

app_name = 'students'

urlpatterns = [
    path("", get_students, name='list_students')
]
