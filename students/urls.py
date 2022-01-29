from django.urls import path
from students.views import get_students

urlpatterns = [
    path("", get_students),
]
