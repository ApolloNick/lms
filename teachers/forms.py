from django.core.exceptions import ValidationError
from django.forms import ModelForm
from teachers.models import Teacher
import django_filters


class TeacherFilter(django_filters.FilterSet):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'email']


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean(self):
        result = super().clean()
        allow_domain = ['gmail', 'example', 'mail', 'yandex', 'ukr']
        email = self.cleaned_data.get('email')
        split_email_first = email.split('@')
        split_email_second = split_email_first[1].split('.')
        if split_email_second[0] not in allow_domain:
            raise ValidationError(f'Sorry, you enter not validated domain. Allowed: {allow_domain}')
        return result

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
    class Meta:
        model = Teacher
        exclude = ['age']
