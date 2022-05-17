from django.core.exceptions import ValidationError
from django.forms import ModelForm
from teachers.models import Teacher
import django_filters


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'age': ['exact']
        }


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data['email']
        has_email_qs = Teacher.objects.filter(email=email)
        if self.instance:
            has_email_qs = has_email_qs.exclude(id=self.instance.id)
        if has_email_qs.exists():
            raise ValidationError("Such email already exists")
        return email


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherEditForm(TeacherBaseForm):
    pass
