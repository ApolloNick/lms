from django.forms import ModelForm
from teachers.models import Teacher


class TeacherCreateForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'occupation', 'email', 'birth_date', 'phone_number']
