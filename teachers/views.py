from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt

from students.utils import render_list
from teachers.forms import TeacherCreateForm
from teachers.models import Teacher


def get_teachers(request):
    qs = Teacher.objects.all()
    params = ['first_name', 'last_name', 'age', 'occupation', 'email', 'birth_date', 'phone_number']
    query = {}

    form = f"""
    <form>
    <p> Search Teachers </p>
    <p>
        <input type="text" name="first_name"
            value="{request.GET.get('first_name', '')}"
            placeholder = "Enter your first name"
    </p>
    <p>
        <input type="text' name="last_name"
            value="{request.GET.get('last_name', '')}"
            placeholder="Enter your last name"
    </p>
    <p>
        <input type="number" name="age"
        value="{request.GET.get('age', '')}"
        placeholder="Enter your number"
    </p>
    <p>
        <input type="number" name="age"
        value="{request.GET.get('occupation', '')}"
        placeholder="Enter your number"
    </p>
    
    </form>
"""

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
    return render_list(qs)


@csrf_exempt
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeacherCreateForm()

    html = f"""
        <form method="post">
            {form.as_p()}
            <p><button type="submit">Create Teacher</button></p>
        </form>
    """

    return HttpResponse(html)

