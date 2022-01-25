import re
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from teachers.models import Teacher


class TeacherBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'(\+\d\d?)?\(\d{3}\)(\d-?){7}$', phone_number):
            raise ValidationError('Phone number has to be like +38(050)111-11-11')
        return phone_number

    def clean_email(self):
        allow_domain = ['gmail', 'example', 'mail', 'yandex', 'ukr']
        email = self.cleaned_data['email']
        split_email_first = email.split('@')
        split_email_second = split_email_first[1].split('.')
        if split_email_second[0] not in allow_domain:
            raise ValidationError(f'Sorry, you enter not validated domain. Allowed: {allow_domain}')
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        if Teacher.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return self.cleaned_data


class TeacherCreateForm(TeacherBaseForm):
    pass


class TeacherEditForm(TeacherBaseForm):
    class Meta:
        model = Teacher
        exclude = ['age']
