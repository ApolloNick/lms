from django.http import HttpResponse
from django.shortcuts import render  # noqa
from students.utils import render_list
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    params = ["first_name", "last_name", "age", "occupation"]
    query = {}
    for param_name in params:
        param_value = request.GET.get(param_name)
        if param_value:
            query[param_name] = param_value
    try:
        qs = qs.filter(**query)
    except ValueError as e:
        return HttpResponse(f"Error occurred. {str(e)} ", status=400)
    return render_list(qs)
