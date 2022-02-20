from django.contrib import admin
from groups.models import Group
from teachers.models import Teacher


class TeacherTable(admin.TabularInline):
    model = Teacher
    fields = ['first_name', 'last_name']
    readonly_fields = fields
    show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'name', 'course', 'start_date']
    inlines = [TeacherTable]


admin.site.register(Group, GroupAdmin)
