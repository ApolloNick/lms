from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from teachers.forms import TeacherCreateForm, TeacherEditForm, TeacherFilter
from teachers.models import Teacher


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
        return context


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherCreateForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/create_teachers.html'


class TeacherEditView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherEditForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('teachers:list_teachers')
    template_name = 'teachers/edit_teachers.html'


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    pk_url_kwarg = 'id'
    template_name = 'teachers/delete_teachers.html'
    success_url = reverse_lazy('teachers:list_teachers')
