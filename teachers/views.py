from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from teachers.forms import TeacherCreateForm, TeacherEditForm, TeacherFilter
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    teacher_filter = TeacherFilter(data=request.GET, queryset=qs)
    return render(request, 'list_teachers.html', {
        "args": request.GET,
        'filter': teacher_filter
    })


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherCreateForm()
    return render(request, 'create_teachers.html', {
        'form': form
    })


@csrf_exempt
def edit_teacher(request, id: int):
    teacher = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list_teachers'))
    else:
        form = TeacherEditForm(instance=teacher)
    return render(request, 'edit_teachers.html', {
        'form': form
    })


@csrf_exempt
def delete_teacher(request, id: int):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list_teachers'))
    return render(
        request,
        'delete_teachers.html',
        {'teacher': teacher}
    )
