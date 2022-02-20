from django.contrib import admin
from teachers.models import Teacher, Course


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'email', 'age']
    search_fields = ['first_name', 'last_name']
    list_filter = ['group']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course)
