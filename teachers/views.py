from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404  # noqa
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from teachers.forms import TeacherCreateForm, TeacherEditForm
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    params = ['first_name', 'last_name', 'age', 'occupation', 'email', 'birth_date', 'phone_number']
    query = {}

    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            if "," in param_value:
                param_values = param_value.split(",")
                query[param_name + "__in"] = param_values
            else:
                query[param_name] = param_value
    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error occurred. {str(e)} ", status=400)
    return render(request, 'list_teachers.html', {
        "args": request.GET,
        'qs': qs
    })


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_teachers'))
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
            return HttpResponseRedirect(reverse('list_teachers'))
    else:
        form = TeacherEditForm(instance=teacher)
    return render(request, 'edit_teachers.html', {
        'form': form
    })
