from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from teachers.forms import TeacherCreateForm, TeacherEditForm, TeacherFilter
from teachers.models import Teacher
import json


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list_teachers.html'

    def get_filter(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return TeacherFilter(data=self.request.GET, queryset=queryset)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('group')
        filter_ = self.get_filter(queryset)
        return filter_.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter()
        paginator = Paginator(self.get_queryset(), 10)
        page_number = self.request.GET.get('page', '1')
        page_obj = paginator.page(int(page_number))
        context['page_obj'] = page_obj
        return context


class TeacherListAPIExample(View):
    def get(self, request):
        queryset = Teacher.objects.all()
        response_dict = {
            'teachers': [
                {'id': teacher.id, 'first_name': teacher.first_name, 'last_name': teacher.last_name,
                 'occupation': teacher.occupation, 'group_obj': teacher.group}
                for teacher in queryset
            ]
        }
        return HttpResponse(json.dumps(response_dict), content_type='application/json')


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/create_teachers.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            "Teacher created successfully"
        )
        return result


class TeacherEditView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherEditForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/edit_teachers.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request,
            "Teacher edited successfully"
        )
        return result


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    pk_url_kwarg = 'id'
    template_name = 'teachers/delete_teachers.html'
    success_url = reverse_lazy('teachers:list_teachers')
