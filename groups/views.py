from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView
from groups.forms import GroupEditForm
from groups.models import Group


def get_group(request, id):
    group = get_object_or_404(Group, id=id)
    return render(
        request,
        'groups/group.html',
        {
            'group': group
        }
    )


class GroupListAPIExample(View):
    def get(self, request):
        import json
        queryset = Group.objects.all()
        response_dict = {
            'group': [
                {'id': group.id, 'name': group.name, 'course': group.course,
                 'start_date': group.start_date}
                for group in queryset
            ]
        }
        return HttpResponse(json.dumps(response_dict), content_type='application/json')


class GroupEditView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupEditForm
    pk_url_kwarg = 'id'
    template_name = 'groups/edit_groups.html'
