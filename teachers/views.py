from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from teachers.forms import TeacherCreateForm, TeacherEditForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    teacher_filter = TeacherFilter(data=request.GET, queryset=qs)
    return render(request, 'teachers/list_teachers.html', {
        "args": request.GET,
        'filter': teacher_filter
    })


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherCreateForm()
    return render(request, 'teachers/create_teachers.html', {
        'form': form
    })


def edit_teacher(request, id: int):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherEditForm(instance=teacher)
    return render(request, 'teachers/edit_teachers.html', {
        'form': form
    })


def delete_teacher(request, id: int):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list_teachers'))
    return render(
        request,
        'teachers/delete_teachers.html',
        {'teacher': teacher}
    )
