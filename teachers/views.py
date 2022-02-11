from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView

from teachers.forms import TeacherCreateForm, TeacherEditForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all().select_related('group')
    teacher_filter = TeacherFilter(data=request.GET, queryset=qs)
    return render(request, 'teachers/list_teachers.html', {
        "args": request.GET,
        'filter': teacher_filter
    })


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/create_teachers.html'


class TeacherEditView(UpdateView):
    model = Teacher
    form_class = TeacherEditForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/edit_teachers.html'


class TeacherDeleteView(DeleteView):
    model = Teacher
    pk_url_kwarg = 'id'
    template_name = 'teachers/delete_teachers.html'
    success_url = reverse_lazy('teachers:list_teachers')
